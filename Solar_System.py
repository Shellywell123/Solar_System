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
    
    def ring(self,ax,name,rmin,rmax,orbit_radius,angluar_orbital_position,orbital_inclination,ring_angle):
        """
        plots planetary gas rings
        """

        image_file = 'Images/surfaces/{}_Rings.jpg'.format(name)
        img        =  plt.imread(image_file)

        count = 100 

        u = np.linspace(0   , 2*np.pi, img.shape[0])
        r = np.linspace(rmin, rmax   , img.shape[1])

        u_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
        r_inds = np.linspace(0, img.shape[1] - 1, count).round().astype(int)

        u = u[u_inds]   
        r = r[r_inds]

        img = img[np.ix_(u_inds, r_inds)]

        x = np.outer(r, np.cos(u))
        y = np.outer(r, np.sin(u))
        h = np.empty(y.shape)
        h.fill(5)

        x,y,z = self.tf.cartesian_transformation_radial(x,y,h,orbit_radius,orbital_inclination,angluar_orbital_position)

        ax.plot_surface(x,y,z, facecolors=img/255, cstride=1, rstride=1,zorder=1,alpha=.5)

    ######################################################################################
            
    def plot_orbit(self,ax,name,colour,orbit_radius,orbital_inclination,orbit_centre=[0,0,0]):
        """
        plots planet orbits
        """
        x_start = orbit_centre[0]
        y_start = orbit_centre[1]
        z_start = orbit_centre[2]

        x_data = []
        y_data = []
        z_data = []
        
        theta = 2*np.pi/100
            
        for i in range(100+1):
            x_orb = x_start + (orbit_radius*np.cos(theta * i))
            y_orb = y_start + (orbit_radius*np.sin(theta * i))
            z_orb = z_start + (x_orb * np.sin(orbital_inclination))
            
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

    def asteroid_belt(self,ax,rmin,rmax,num_of_asteroids,orbital_inclination):
        """
        scatter plots an asteroid belt
        """

        orbital_inclination = self.tf.degrees_to_radians(orbital_inclination)

        theta = float(2*np.pi/1000)
        for i in range(int(num_of_asteroids)+1):
            theta = theta+random.randint(-int(np.pi/1000),int(np.pi/1000))
            r = random.randint(int(rmin),int(rmax))
            x_ast = r*np.cos(theta * i)
            y_ast = r*np.sin(theta * i)
            z_ast = x_ast * np.sin(orbital_inclination)
            
            s = random.randint(1,4)                
            ax.scatter(x_ast,y_ast,z_ast,color='grey',s=s)
        print(' - Created Asteroid Belt')

    ######################################################################################

    def satelite(self,ax,name,moon_radius,moon_orbit_radius,host_orbit_radius,host_angluar_orbital_position,host_orbital_inclination):
        """
        makes a satelite to a planet
        """
        
        moon_orbital_inclination      = 0
        moon_angluar_orbital_position = 0


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
        x,y,z = self.tf.spherical_to_cartesian(theta,phi,moon_radius)

        #sun to planet
        x,y,z = self.tf.cartesian_transformation_radial(x,y,z,host_orbit_radius,host_orbital_inclination,host_angluar_orbital_position)
        
        x_orb,y_orb,z_orb = [0,0,0]         
        x_orb,y_orb,z_orb = self.tf.cartesian_transformation_radial(x_orb,y_orb,z_orb,host_orbit_radius,host_orbital_inclination,host_angluar_orbital_position)
        self.plot_orbit(ax,name,'grey',moon_orbit_radius,moon_orbital_inclination,orbit_centre=[x_orb,y_orb,z_orb])
 
        # planet to moon
        x,y,z = self.tf.cartesian_transformation_radial(x,y,z,moon_orbit_radius,moon_orbital_inclination,moon_angluar_orbital_position)

        ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1,zorder=2,alpha=.5)    
        
    ######################################################################################
     
    def planet(self,ax,name,orbit_colour,ring,moons,orbit_radius,body_radius,orbital_inclination):
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
        
        extras = ''

        if orbit_radius != 0:
            orbit_radius,obliquity,angluar_orbital_position=self.calculate_position_and_orientation(date,hour,orbit_radius,obliquity,orbit_duration_days)
            self.plot_orbit(ax,name,orbit_colour,orbit_radius,orbital_inclination)
            #orbital position
            x,y,z = self.tf.cartesian_transformation_radial(x,y,z,orbit_radius,orbital_inclination,angluar_orbital_position)

            #check for moons
            if moons != 'no':
                name,moon_radius,moon_orbit_radius = moons
                moon_orbit_radius = moon_orbit_radius + body_radius
                self.satelite(ax,name,moon_radius,moon_orbit_radius,orbit_radius,angluar_orbital_position,orbital_inclination)
                extras = extras + '+ Moon'

            #check for rings
            if ring != 'no':            
                rmin,rmax,ring_angle = ring
                rmin = rmin+body_radius
                rmax = rmax+body_radius
                self.ring(ax,name,rmin,rmax,orbit_radius,angluar_orbital_position,orbital_inclination,ring_angle)
                extras = extras + '+ Rings'

        ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1,zorder=2,alpha=.5)    
        print(' - Created {} {}'.format(name,extras))

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
        
        #if scaling != 'Accurate':
        # scalings (first two letters + s)
        gen_scaling_factor = 2000
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

        # moon info
        #        name,moon_radius,moon_orbit_radius
        e_moon = 'Moon',1737*eas,384402

        # ring info
        #        rmin                  ,rmax                  ,ring_angle
        s_ring = 7e3*sas,8e4*sas,1

        #    planet(ax, name      ,orbit_colour   ,ring   ,moons   ,rsolar ,rplan      ,orbtilt)
        
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
        

        self.asteroid_belt(ax,3e9,45e8,1000,25)

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
