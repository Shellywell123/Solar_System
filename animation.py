from Solar_System import PySpace
import matplotlib.pyplot as plt
import numpy as np
import os

################################################################################
# begining of class
################################################################################

class PyAnimate:

    def __init__(self):
        """
        class initaliser
        """
        self.ss = PySpace()

        print('#'*55)
        print(' PyAnimate initalised '+self.ss.get_live_time())
        print('#'*55)

    ######################################################################################

    def frames_to_gif(self,gifname):
        """
        converts all images in frames dir to a gif
        """
        import imageio
        images = []
        for filename in os.listdir('Images/frames/'):
            images.append(imageio.imread('Images/frames/'+filename))
        filename = 'Images/gifs/{}.gif'.format(gifname)
        imageio.mimsave(filename, images)
        print('{} made'.format(filename))

    ######################################################################################

    def make_spin_gif(self,num_of_frames=70):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for azim in list(np.linspace(0,360,num_of_frames)):
            self.ss.solar_system(scaling='notoscale',POV=[azim,30,15e7],show='noshow')

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('spin')

    ######################################################################################

    def make_zoom_out_gif(self,num_of_frames=50):
        """
        create a gif of the system zooming out radially
        """

        i = 1
        for max_lim in list(np.geomspace(6.5e7, 3e9, num=num_of_frames)):
            self.ss.solar_system(scaling='notoscale',POV=[-60,30,max_lim],show='noshow')

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('zoomout')


    ######################################################################################

    def make_spiral_out_gif(self,num_of_frames=50):
        """
        create a gif of the system zooming out radially
        """

        i = 1
        max_lim_list = list(np.geomspace(12e6, 1e10,num_of_frames))
        azim_list    = list(np.linspace(-180,180,num_of_frames))

        for i in range(0,num_of_frames):

            azim    = azim_list[i]
            max_lim = max_lim_list[i]

            self.ss.solar_system(scaling='notoscale',POV=[azim,30,max_lim],show='noshow')

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('spiralout')

################################################################################
# End of class
################################################################################
