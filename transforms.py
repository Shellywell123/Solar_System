# -*- coding: utf-8 -*
"""
Created on Tues Sep 22 22:23:56 2020

@author: B E N
"""

import numpy as np

################################################################################
# begining of class
################################################################################

class PyTransforms:

    def __init__(self):
        """
        class initaliser
        """
        # commented out as is used very often
        # print('#'*55)
        # print(' PyAnimate initalised '+self.get_live_time())
        # print('#'*55)
        pass

    ######################################################################################
    
    def degrees_to_radians(self,angle):
        """
        degrees to radians angle converter
        """
        angle = float(angle/180)*np.pi
        return angle

    ######################################################################################
                
    def spherical_to_cartesian(self,theta,phi,radius):
        """
        simple spherical to cartesian coord transform
        """
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        return x,y,z

    ######################################################################################
    
    def cartesian_transformation_obliquity(self,x,y,z,obliquity):
        """
        converts cartesian coords to cartesian coords with a obliquity tilt 
        """
        obliquity = self.degrees_to_radians(-obliquity)
        z =  z*np.cos(obliquity) + x*np.sin(obliquity)
        x = -z*np.sin(obliquity) + x*np.cos(obliquity)
        return x,y,z

    ######################################################################################
    
    def spherical_to_cartesian(self,theta,phi,radius):
        """
        simple spherical to cartesian coord transform
        """
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        return x,y,z
        
    ######################################################################################
    
    def cartesian_transformation_radial(self,x,y,z,orbit_radius,orbital_inclination,angluar_orbital_position):
        """
        orbiatal position and inclination transformations
        """
        orbital_inclination = self.degrees_to_radians(orbital_inclination)

        x = x + orbit_radius*np.cos(angluar_orbital_position)
        y = y + orbit_radius*np.sin(angluar_orbital_position)
        z = z
        return x,y,z

################################################################################
# End of class
################################################################################
