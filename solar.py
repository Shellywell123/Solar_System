import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def orbit(r,n):
    """ """
    x_list = []
    y_list = []
    
    x=np.linspace(0,n)
    y=np.linspace(0,n)
    for i in range(0,n):
        if (x[i]*x[i] + y[i]*y[i] == r[i]*r[i]):
            print(x[i], " " , y[i])
            
            x_list.append(x[i])
            y_list.append(y[i])
        
    return x_list,y_list
    

fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.plot(orbit(1,100))
#Axes3D.show()
plt.show()