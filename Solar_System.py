import matplotlib
matplotlib.use('TkAgg')
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
    
    def rings_dict(self,ax,rings_info,host_info):
        """
        plots planetary gas rings
        """

        ##############################################################
        # unpack rings info
        ##############################################################
        
        rmin             = rings_info['minimum_ring_radius']
        rmax             = rings_info['maximum_ring_radius']
        ring_inclination = rings_info['ring_inclination']

        ##############################################################
        # unpack host info
        ##############################################################

        host_name                     = host_info['host_name']
        host_orbit_radius             = host_info['host_orbit_radius']
        host_angluar_orbital_position = host_info['host_angluar_orbital_position']
        host_orbital_inclination      = host_info['host_orbital_inclination']

        moon_orbital_inclination      = 0
        moon_angluar_orbital_position = 0
        image_file = 'Images/surfaces/planets/{}_Rings.jpg'.format(host_name)
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

        x,y,z = self.tf.cartesian_transformation_radial(x,y,h,host_orbit_radius,host_orbital_inclination,host_angluar_orbital_position)
        ax.plot_surface(x,y,z, facecolors=img/255, cstride=1, rstride=1,zorder=1,alpha=.5)

    ######################################################################################
            
    def plot_orbit(self,ax,name,colour,orbit_radius,orbital_inclination,orbit_centre=[0,0,0],label='yes'):
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
        
        if label == 'no':
            ax.plot(x_data,y_data,z_data,color=colour,linewidth=1,linestyle='--')

        if label == 'yes':
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

    def satelite_dict(self,ax,moon_info,host_info):
        """
        makes a satelite to a planet
        """

        ##############################################################
        # unpack moon info
        ##############################################################
        
        moon_name         = moon_info['moon_name']
        moon_radius       = moon_info['moon_radius']
        moon_orbit_radius = moon_info['moon_orbit_radius']

        host_orbit_radius             = host_info['host_orbit_radius']
        host_angluar_orbital_position = host_info['host_angluar_orbital_position']
        host_orbital_inclination      = host_info['host_orbital_inclination']

        moon_orbital_inclination      = 0
        moon_angluar_orbital_position = 0


        image_file = 'Images/surfaces/moons/{}.jpg'.format(moon_name)
       # image_file = 'Images/surfaces/moons/Moon.jpg'
        img = plt.imread(image_file)

        # define a grid matching the map size, subsample along with pixel    
        theta = np.linspace(0, np.pi, img.shape[0])
        rot = 0
        phi  = np.linspace(0+rot, 2*np.pi+rot, img.shape[1])

        count = 100 # keep 180 points along theta and phi

        theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
        phi_inds   = np.linspace(0, img.shape[1] - 1, count).round().astype(int)

        theta = theta[theta_inds]   
        phi   = phi[phi_inds]

        img = img[np.ix_(theta_inds, phi_inds)]

        theta,phi = np.meshgrid(theta, phi)
        
        ##############################################################
        # coord trandforms
        ##############################################################

        #spherical
        x,y,z = self.tf.spherical_to_cartesian(theta,phi,moon_radius)

        #sun to planet
        x,y,z = self.tf.cartesian_transformation_radial(x,y,z,host_orbit_radius,host_orbital_inclination,host_angluar_orbital_position)
        
        x_orb,y_orb,z_orb = [0,0,0]         
        x_orb,y_orb,z_orb = self.tf.cartesian_transformation_radial(x_orb,y_orb,z_orb,host_orbit_radius,host_orbital_inclination,host_angluar_orbital_position)
        self.plot_orbit(ax,moon_name,'grey',moon_orbit_radius,moon_orbital_inclination,orbit_centre=[x_orb,y_orb,z_orb],label='no')
 
        # planet to moon
        x,y,z = self.tf.cartesian_transformation_radial(x,y,z,moon_orbit_radius,moon_orbital_inclination,moon_angluar_orbital_position)

        ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1,zorder=2,alpha=.5)    
        
    ######################################################################################
     
    def planet_dict(self,ax,planet_info):
        """
        plots planets
        """

        ##############################################################
        # unpack planet info
        ##############################################################
        
        name                = planet_info['name']
        orbit_colour        = planet_info['orbit_colour']
        rings_info          = planet_info['rings_info']
        moons_info          = planet_info['moons_info']
        orbit_radius        = planet_info['orbit_radius']
        body_radius         = planet_info['body_radius']
        orbital_inclination = planet_info['orbital_inclination']
                            
        date = '1'
        hour = 1
        obliquity = 0
        orbit_duration_days = 1

        ##############################################################
        # convert angles to radians
        ##############################################################
        
        obliquity           = self.tf.degrees_to_radians(obliquity)
        orbital_inclination = self.tf.degrees_to_radians(orbital_inclination)
    
        image_file = 'Images/surfaces/planets/{}.jpg'.format(name)
        img = plt.imread(image_file)

        # define a grid matching the map size, subsample along with pixel    
        theta = np.linspace(0, np.pi, img.shape[0])
        rot = 0
        phi  = np.linspace(0+rot, 2*np.pi+rot, img.shape[1])

        count = 100 # keep 180 points along theta and phi

        theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
        phi_inds   = np.linspace(0, img.shape[1] - 1, count).round().astype(int)

        theta = theta[theta_inds]   
        phi   = phi[phi_inds]

        img = img[np.ix_(theta_inds, phi_inds)]

        theta,phi = np.meshgrid(theta, phi)
        
        ##############################################################
        # coord transforms
        ##############################################################

        #spherical
        x,y,z = self.tf.spherical_to_cartesian(theta,phi,body_radius)
        #body tilt
        x,y,z = self.tf.cartesian_transformation_obliquity(x,y,z,obliquity)
        
        extras = str()

        if orbit_radius != 0:

            orbit_radius,obliquity,angluar_orbital_position=self.calculate_position_and_orientation(date,hour,orbit_radius,obliquity,orbit_duration_days)
            self.plot_orbit(ax,name,orbit_colour,orbit_radius,orbital_inclination)
            #orbital position
            x,y,z = self.tf.cartesian_transformation_radial(x,y,z,orbit_radius,orbital_inclination,angluar_orbital_position)

            ##################################################
            # moons check
            ##################################################
        
            if moons_info != 'no':
                for moon_info in moons_info:

                    host_info = {'host_name'                    : name,
                                'host_orbit_radius'            : orbit_radius,
                                'host_angluar_orbital_position' : angluar_orbital_position,
                                'host_orbital_inclination'      : orbital_inclination}

                    #self.satelite(ax,moon_name,moon_radius,moon_orbit_radius,orbit_radius,angluar_orbital_position,orbital_inclination)
                    self.satelite_dict(ax,moon_info,host_info)

                    moon_name = moon_info['moon_name']
                    extras    = extras + ' + ' + moon_name

            ##################################################
            # rings check
            ##################################################
        
            if rings_info != 'no':            

                rings_info['minimum_ring_radius'] = rings_info['minimum_ring_radius'] + body_radius
                rings_info['maximum_ring_radius'] = rings_info['maximum_ring_radius'] + body_radius
           
                host_info = {'host_name'                    : name,
                            'host_orbit_radius'            : orbit_radius,
                            'host_angluar_orbital_position' : angluar_orbital_position,
                            'host_orbital_inclination'      : orbital_inclination}

               # self.ring(ax,name,rmin,rmax,orbit_radius,angluar_orbital_position,orbital_inclination,ring_angle)
                self.rings_dict(ax,rings_info,host_info)
                extras = extras + ' + Rings'

        ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1,zorder=2,alpha=.5)    
        print(' - Created {}{}'.format(name,extras))

    #####################################################
    
    def starry_night(self,ax,max_lim,num_of_Stars):
        """
        plots random stars in foreground and background
        """
        max_lim = int(max_lim)
        
        random.seed(1)

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
    
    def solar_system(self,scaling='scaled',show='show',grid='nogrid',POV={'azim':-60,'elev':30,'max_lim':2.5e9}):
        """
        creates solarsystems
        """        

        ##############################################################
        # unpack camera point of view
        ##############################################################
        
        azim    = POV['azim']
        elev    = POV['elev']
        max_lim = POV['max_lim']

        min_lim = -max_lim

        fig = plt.figure(0,figsize=plt.figaspect(0.5)*1.5)
        fig.canvas.set_window_title('Solar System')
        
        try:
            # no point with this until can sort scaling issue
            pass
            # mng = plt.get_current_fig_manager()
            # plt.rcParams['toolbar'] = 'None'
            # #fig.canvas.window().statusBar().setVisible(False)
            # # fig.canvas.toolbar.pack_forget()
            # # mng.window.showMaximized()
            # # mng.resize(*mng.window.maxsize())
            # mng.full_screen_toggle()

            # plt.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
            # fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)

            # manager = plt.get_current_fig_manager()
            # manager.full_screen_toggle()
        except:
            print('failed to go full screen')
            pass

        ax = fig.add_subplot(111,projection='3d',azim=azim, elev=elev)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        ##############################################################
        # plot background
        ##############################################################
        
        fig.set_facecolor('black')
        ax.set_facecolor('black')
        ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
        
        ##############################################################
        # make solar system
        ##############################################################
        
        from data import PyData
        d = PyData(scaling)
        sun      = self.planet_dict(ax,d.sun_info)
        mercury  = self.planet_dict(ax,d.mercury_info)
        venus    = self.planet_dict(ax,d.venus_info)
        earth    = self.planet_dict(ax,d.earth_info)
        mars     = self.planet_dict(ax,d.mars_info)
        ast_belt = self.asteroid_belt(ax,3e9,45e8,1000,25)  
        jupiter  = self.planet_dict(ax,d.jupiter_info)
        saturn   = self.planet_dict(ax,d.saturn_info)
        uranus   = self.planet_dict(ax,d.uranus_info)
        neptune  = self.planet_dict(ax,d.neptune_info)
        pluto    = self.planet_dict(ax,d.pluto_info)
        stars    = self.starry_night(ax,max_lim*5,2000)
        
        ##############################################################
        # set plot lims
        ##############################################################
        
        ax.set_xlim3d([min_lim,max_lim])
        ax.set_xlabel('km')
        
        ax.set_ylim3d([min_lim,max_lim])
        ax.set_ylabel('km')
        
        ax.set_zlim3d([min_lim,max_lim])
        ax.set_zlabel('km')
        
        ##############################################################
        # axis preferences
        ##############################################################
        
        if grid != 'grid':
            ax.grid(False)
        else:
            plt.rcParams['grid.color'] = "darkgreen"
            ax.grid(color='green',linewdith=1, alpha=0.1)

        ax.spines['bottom'].set_color(  'lime')
        ax.spines['top'].set_color(     'lime')
        ax.xaxis.label.set_color(       'lime')

        ax.tick_params(axis='x', colors='lime')
        ax.tick_params(axis='y', colors='lime')
        ax.tick_params(axis='z', colors='lime')
        ax.auto_scale_xyz(1080,1920)
    #    ax.set_aspect(aspect='equal')
        
        ##############################################################
        # legend preferences
        ##############################################################
        
        leg = ax.legend(loc='upper left', facecolor='none')
        for text in leg.get_texts():
            text.set_color('w')
        
        ##############################################################
        # show option
        ##############################################################
        
        if show == 'show':
            print('Opening GUI...')
            plt.show()
            print(' ...Closed.')

################################################################################
# End of class
################################################################################
