## -*- coding: utf-8 -*-
#"""
#Created on Thu Dec 26 22:56:06 2019
#
#@author: B E N
#"""
#
#import matplotlib.pyplot as plt
#import numpy as np
#
#def planet(ax,colour,orbit_radius, r,angle):
#    """
#    
#    """
#   # plot_orbit(ax,colour,orbit_radius, angle)
#
#    x_data = []
#    y_data = []
#    z_data = []
#    
#    theta = 2*np.pi/10
#    phi = np.pi/10
#    
#    for i in range(10):
#        for j in range(10):
#            
#            x = r*np.cos(theta * i)*np.sin(phi * j)
#            y = r*np.sin(theta * i)*np.sin(phi * j)
#            z = r*np.cos(phi * j) + r * np.sin(angle)
#            
#            x = x + orbit_radius
#            
#            x_data.append(x)
#            y_data.append(y)
#            z_data.append(z)
#            
#    ax.plot_surface(x_data,y_data,z_data)#,color = colour)
#    
#fig = plt.figure()
#    #ax = plt.gca()
#    
#ax = fig.add_subplot(111, projection='3d')
#planet(ax,'k',0,5,0)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u, v = np.mgrid[0:np.pi:50j, 0:2*np.pi:50j]

strength = u
norm=colors.Normalize(vmin = np.min(strength),
                      vmax = np.max(strength), clip = False)

x = 10 * np.sin(u) * np.cos(v)
y = 10 * np.sin(u) * np.sin(v)
z = 10 * np.cos(u)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False,
                       facecolors=cm.coolwarm(norm(strength)))

plt.show()
#.show()