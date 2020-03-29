# -*- coding: utf-8 -*
"""
Created on Mon Dec 23 18:29:56 2019

@author: B E N
"""

import matplotlib.pyplot as plt
from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import numpy as np

###############################################################################

def plot_ring(ax,colour,orbit_radius,ring_radius,angle,ring_angle):
    """
    
    """
    x_data = []
    y_data = []
    z_data = []
    
    theta = 2*np.pi/100
    
    
    for i in range(100+1):
        x_orb = orbit_radius + ring_radius*np.cos(theta * i)
        y_orb = ring_radius*np.sin(theta * i)
        z_orb = orbit_radius*np.sin(angle) #+  np.sin(ring_angle)
        
        x_data.append(x_orb)
        y_data.append(y_orb)
        z_data.append(z_orb)
            
    ax.plot(x_data,y_data,z_data,color=colour,linewidth=2)
    
###############################################################################

def plot_orbit(ax,colour,orbit_radius,angle):
    """
    
    """
    x_data = []
    y_data = []
    z_data = []
    
    theta = 2*np.pi/100
    
    
    for i in range(100+1):
        x_orb = orbit_radius*np.cos(theta * i)
        y_orb = orbit_radius*np.sin(theta * i)
        z_orb = x_orb * np.sin(angle)
        
        x_data.append(x_orb)
        y_data.append(y_orb)
        z_data.append(z_orb)
            
    ax.plot(x_data,y_data,z_data,color=colour,linewidth=1,linestyle='--')
    

###############################################################################
    
def planet(ax,name,colour,ring,moons,orbit_radius, r,angle):
    """
    
    """
    angle = np.radians(angle)
    plot_orbit(ax,colour,orbit_radius, angle)

    x_data = []
    y_data = []
    z_data = []
    
    theta = 2*np.pi/10
    phi = np.pi/10
    
    for i in range(10):
        for j in range(10):
            
            x = r*np.cos(theta * i)*np.sin(phi * j)
            y = r*np.sin(theta * i)*np.sin(phi * j)
            z = r*np.cos(phi * j) + np.sin(angle)*orbit_radius
            
            x = x + orbit_radius
            
            x_data.append(x)
            y_data.append(y)
            z_data.append(z)
            
    ax.scatter(x_data,y_data,z_data,color = colour,label=name)
    
    if ring != 'no':
        
        ring_radius,ring_angle = ring
        plot_ring(ax,colour,orbit_radius,ring_radius,angle,ring_angle)

###############################################################################
        
def starry_night(ax,max_lim,num_of_Stars):
    """
    
    Returns
    -------
    None.

    """
    
    ax.set_facecolor('black')
    
    ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.grid(False)
    
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

###############################################################################

def solar_system(grid):
    """
    
    """
    plt.clf()
    fig = plt.figure('Solar System')
    #ax = plt.gca()
    
    ax = fig.add_subplot(111, projection='3d')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fig.set_facecolor('black')
    
    
    if grid != 'grid':
        ax.grid(False)
    
    ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    
    ring    = 80000000,1
    
    #body   =planet(ax,colur,ring,moons,rsolar,rplan,orbtilt)
    
    Sun     = planet(ax ,'Sun'     ,'gold'        ,'no' ,'no' ,0       ,605000 ,0)
    Mercury = planet(ax ,'Mercury' ,'peru'        ,'no' ,'no' ,46e6    ,2440   ,7.005)
    Venus   = planet(ax ,'Venus'   ,'goldenrod'   ,'no' ,'no' ,107e6   ,6052   ,3.3947)
    Earth   = planet(ax ,'Earth'   ,'forestgreen' ,'no' ,'no' ,1147e6  ,6378   ,0)
    Mars    = planet(ax ,'Mars'    ,'firebrick'   ,'no' ,'no' ,205e6   ,3397   ,1.851)
    Jupiter = planet(ax ,'Jupiter' ,'sandybrown'  ,'no' ,'no' ,741e6   ,71492  ,1.305)
    Saturn  = planet(ax ,'Saturn'  ,'yellow'      ,ring ,'no' ,1.35e9  ,60268  ,2.484)
    Uranus  = planet(ax ,'Uranus'  ,'powderblue'  ,'no' ,'no' ,2.75e9  ,25559  ,0.770)
    Neptune = planet(ax ,'Neptune' ,'dodgerblue'  ,'no' ,'no' ,4.45e9  ,24766  ,1.769)
    Pluto   = planet(ax ,'Pluto'   ,'dimgrey'     ,'no' ,'no' ,4.46e9  ,1150   ,17.142) 
      

    
    max_lim =  5e9
    min_lim = -max_lim
    
    starry_night(ax,max_lim*5,6000)
    
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
    
    # path = "C://Users//benja//Documents//Programming//Python Projects//Solar_System//stars.png"
    
    # fn = get_sample_data(path, asfileobj=False)
    # arr = read_png(fn)
    # height, width = arr.shape[:2]
    # stepX, stepY = 10e9/width, 10e9/height
    
    # X1 = np.arange(-5e9, 5e9, stepX)
    # Y1 = np.arange(-5e9, 5e9, stepY)
    # X1, Y1 = np.meshgrid(X1, Y1)
    # ax.plot_surface(X1, Y1, np.atleast_2d(-5e9), rstride=1, cstride=1, facecolors=arr)
        
   # ax.show() 

###############################################################################

solar_system('no_grid')