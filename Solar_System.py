# -*- coding: utf-8 -*
"""
Created on Mon Dec 23 18:29:56 2019

@author: B E N
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from transforms import PyTransforms
import numpy as np
import random
import os

################################################################################
# begining of class
################################################################################

class PySpace:

    def __init__(self):
        """
        class initaliser
        """
        self.tf = PyTransforms()

        print('#'*55)
        print(' PySpace initalised '+self.get_live_time())
        print('#'*55)

    ######################################################################################
    
    def get_live_time(self):
        """
        returns live time and date for uk
        """
        date     = str(os.popen("date +%D").readlines())[2:-4]
        time     = str(os.popen("date +%T").readlines())[2:-7]
        timezone = str(os.popen("date +%:z").readlines())[2:-7]

        live = time + ' ' + timezone + ' ' + date
        return live

    ######################################################################################
    
    def plot_ring(self,ax,colour,orbit_radius,ring_radius,orbital_inclination,ring_angle):
        """
        plots planetary gas rings
        """
        x_data = []
        y_data = []
        z_data = []
        
        theta = 2*np.pi/100
                
        for i in range(100+1):
            x_orb = orbit_radius + ring_radius*np.cos(theta * i)
            y_orb = ring_radius*np.sin(theta * i)
            z_orb = orbit_radius*np.sin(orbital_inclination) #+  np.sin(ring_angle)
            
            x_data.append(x_orb)
            y_data.append(y_orb)
            z_data.append(z_orb)
                
        ax.plot(x_data,y_data,z_data,color=colour,linewidth=2)

    ######################################################################################
            
    def plot_orbit(self,ax,name,colour,orbit_radius,orbital_inclination):
        """
        plots planet orbits
        """
        x_data = []
        y_data = []
        z_data = []
        
        theta = 2*np.pi/100
            
        for i in range(100+1):
            x_orb = orbit_radius*np.cos(theta * i)
            y_orb = orbit_radius*np.sin(theta * i)
            z_orb = x_orb * np.sin(orbital_inclination)
            
            x_data.append(x_orb)
            y_data.append(y_orb)
            z_data.append(z_orb)
                
        ax.plot(x_data,y_data,z_data,color=colour,linewidth=1,linestyle='--',label=name)

    ######################################################################################
    
    def calculate_position_and_orientation(self,date,hour,orbit_radius,obliquity,orbit_duration_days):
        """
        calculates the orbital position of a body given a date
        """

        #currently centered around earth
        
        day = int(date.split('/')[0])
        
        # to be made correct 
        angluar_orbital_position = (float(day+(hour/24.))/orbit_duration_days)*np.pi*2

        # to be made correct should always face earth
        obliquity = obliquity

        #to be made elliptical
        orbit_radius=orbit_radius

        return orbit_radius,obliquity,angluar_orbital_position

    ######################################################################################

    def asteroid_belt(self):
        """
        INCOMPLETE
        """
        pass

    ######################################################################################

    def satelite(self):
        """
        INCOMPLETE
        """
        pass

    ######################################################################################
     
    def planet(self,ax,name,colour,ring,moons,orbit_radius,body_radius,orbital_inclination):
        """
        plots planets
        """

        date = '1'
        hour = 1
        obliquity = 0
        orbit_duration_days = 1

        # make angles rads
        obliquity           = self.tf.degrees_to_radians(obliquity)
        orbital_inclination = self.tf.degrees_to_radians(orbital_inclination)
    
        image_file = 'Images/surfaces/{}.jpg'.format(name)
        img = plt.imread(image_file)

        # define a grid matching the map size, subsample along with pixel    
        theta = np.linspace(0, np.pi, img.shape[0])
        rot = 0
        phi  = np.linspace(0+rot, 2*np.pi+rot, img.shape[1])

        count = 180 # keep 180 points along theta and phi

        theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
        phi_inds   = np.linspace(0, img.shape[1] - 1, count).round().astype(int)

        theta = theta[theta_inds]   
        phi   = phi[phi_inds]

        img = img[np.ix_(theta_inds, phi_inds)]

        theta,phi = np.meshgrid(theta, phi)
        
        # transformations
        #spherical
        x,y,z = self.tf.spherical_to_cartesian(theta,phi,body_radius)
        #body tilt
        x,y,z = self.tf.cartesian_transformation_obliquity(x,y,z,obliquity)
        

        if orbit_radius != 0:
            orbit_radius,obliquity,angluar_orbital_position=self.calculate_position_and_orientation(date,hour,orbit_radius,obliquity,orbit_duration_days)
            self.plot_orbit(ax,name,colour,orbit_radius,orbital_inclination)
            #orbital position
            x,y,z = self.tf.cartesian_transformation_radial(x,y,z,orbit_radius,orbital_inclination,angluar_orbital_position)


        ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1)
        print(' - Created', name)

        #check for moons
        if moons != 'no':
            self.satelite()

        #check for rings
        if ring != 'no':
            
            ring_radius,ring_angle = ring
            self.plot_ring(ax,colour,orbit_radius,ring_radius,orbital_inclination,ring_angle)

    ######################################################################################
    
    def starry_night(self,ax,max_lim,num_of_Stars):
        """
        plots random stars in foreground and background
        """
        max_lim = int(max_lim)
        
        random.seed(1)

        ax.set_facecolor('black')
        
        ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        
        x1 = []
        x2 = []
        x3 = []
        
        min_lim = -max_lim
        
        s = random.randrange(start=1, stop=3)
        
        for i in range(int(num_of_Stars/6)):
            x1.append(random.randrange(start=min_lim, stop=max_lim))
            x2.append(random.randrange(start=min_lim, stop=max_lim))
            x3.append(min_lim)
        
        ax.scatter(x1, x2, x3, c='white', s=s)
        ax.scatter(x2, x3, x1, c='white', s=s)
        ax.scatter(x3, x1, x2, c='white', s=s)
        
        for i in range(int(num_of_Stars/6)):
            x1.append(random.randrange(start=min_lim, stop=max_lim))
            x2.append(random.randrange(start=min_lim, stop=max_lim))
            x3.append(max_lim)
        
        ax.scatter(x1, x2, x3, c='white', s=s)
        ax.scatter(x2, x3, x1, c='white', s=s)
        ax.scatter(x3, x1, x2, c='white', s=s)
        print(' - Created Stars')
        
    ######################################################################################
    
    def solar_system(self,grid,max_lim=2.5e9,show='show'):
        """
        creates solarsystems
        """
       
        fig = plt.figure(0)
        fig.canvas.set_window_title('Solar System')
        
        try:
            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())
        except:
            pass

        ax = fig.add_subplot(111, projection='3d')
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        fig.set_facecolor('black')
        
        
        if grid != 'grid':
            ax.grid(False)
        else:
            plt.rcParams['grid.color'] = "darkgreen"
            ax.grid(color='green',linewdith=1, alpha=0.1)
        
        ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        
        # moon info
        #        name,moon_radius,moon_orbit_radius
        e_moon = 'Moon',

        # ring info
        #        ring_radius,ring_angle
        s_ring = 80000000   ,1


        # scalings (first two letters + s)
        gen_scaling_factor = 4000
        sus = gen_scaling_factor*0.015
        mes = gen_scaling_factor
        ves = gen_scaling_factor
        eas = gen_scaling_factor
        mas = gen_scaling_factor
        jus = gen_scaling_factor
        sas = gen_scaling_factor
        urs = gen_scaling_factor
        nes = gen_scaling_factor
        pls = gen_scaling_factor

        #    planet(ax, name      ,colour        ,ring   ,moons   ,rsolar ,rplan      ,orbtilt)
        
        self.planet(ax ,'Sun'     ,'gold'        ,'no'   ,'no'    ,0      ,605000*sus ,0)
        self.planet(ax ,'Mercury' ,'peru'        ,'no'   ,'no'    ,46e6   ,2440*mes   ,7.005)
        self.planet(ax ,'Venus'   ,'goldenrod'   ,'no'   ,'no'    ,107e6  ,6052*ves   ,3.3947)
        self.planet(ax ,'Earth'   ,'forestgreen' ,'no'   , e_moon ,149e6  ,6378*eas   ,0)
        self.planet(ax ,'Mars'    ,'firebrick'   ,'no'   ,'no'    ,205e6  ,3397*mas   ,1.851)
        self.planet(ax ,'Jupiter' ,'sandybrown'  ,'no'   ,'no'    ,741e6  ,71492*jus  ,1.305)
        self.planet(ax ,'Saturn'  ,'yellow'      ,s_ring ,'no'    ,1.35e9 ,60268*sas  ,2.484)
        self.planet(ax ,'Uranus'  ,'powderblue'  ,'no'   ,'no'    ,2.75e9 ,25559*urs  ,0.770)
        self.planet(ax ,'Neptune' ,'dodgerblue'  ,'no'   ,'no'    ,4.45e9 ,24766*nes  ,1.769)
        self.planet(ax ,'Pluto'   ,'dimgrey'     ,'no'   ,'no'    ,4.46e9 ,1150*pls   ,17.142) 
        
        # max_lim = 205e6
        min_lim = -max_lim
        
        self.starry_night(ax,max_lim*5,2000)
        
        ax.set_xlim3d([min_lim,max_lim])
        ax.set_xlabel('km')
        
        ax.set_ylim3d([min_lim,max_lim])
        ax.set_ylabel('km')
        
        ax.set_zlim3d([min_lim,max_lim])
        ax.set_zlabel('km')
        
        ax.spines['bottom'].set_color(  'lime')
        ax.spines['top'].set_color(     'lime')
        ax.xaxis.label.set_color(       'lime')
        ax.tick_params(axis='x', colors='lime')
        ax.tick_params(axis='y', colors='lime')
        ax.tick_params(axis='z', colors='lime')
        
        leg = ax.legend(loc='upper left', facecolor='none')
        for text in leg.get_texts():
            text.set_color('w')
        
        if show == 'show':
            plt.show()

################################################################################
# End of class
################################################################################
