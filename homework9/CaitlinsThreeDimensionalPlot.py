import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

#a cosine version of the sine example (diff colors for awesomeness)
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.cos(r)

surf = ax.plot_surface(x, y, z, cmap = cm.cool, linewidth = 0, antialiased = False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink = 0.5, aspect = 5)

plt.show()

def cosine_function_3d(x, y):
    """
    Takes an x array and y array and creates a cosine graph.
    Input: x, y (arrays of numbers that will become x and y values for the points graphed)
    Output: a cosine graph (of ranging size based on x and y)
    """
    
    #create a graph
    fig = plt.figure(figsize = (10, 10))

    #make the figure a 3 dimensional graph
    ax = fig.add_subplot(projection = "3d")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3 Dimensional Cosine Function")

    #create r (radius, x and y as one value) to easier create z values
    plot_x, plot_y = np.meshgrid(x, y)
    r = np.sqrt(plot_x**2 + plot_y**2)

    #generate z values
    z = np.cos(r)

    #create the surface (cmap = cm.gist_rainbow makes it rainbow colored based on z-values, linewidth = 0 makes it lineless, antialiased = false makes it opaque)
    surf = ax.plot_surface(x, y, z, label = "cosine function", cmap = cm.gist_rainbow, linewidth = 0, antialiased = False)

    #set upper and lower values for the z-axis (-50 and 50)
    ax.set_zlim(-10, 10)

    #Adds 10 evenly spaced ticks on the z-axis for measurement
    ax.zaxis.set_major_locator(LinearLocator(10))

    #sets the format for the ticks on the z-axis (no decimal places)
    ax.zaxis.set_major_formatter('{x:.0f}')

    #create the color bar to tell what values each color represents
    fig.colorbar(surf, shrink = 0.5, aspect = 8, pad = 0.5)

    #create a legend
    ax.legend(loc = "right", bbox_to_anchor = (1.5, 1.2))

    plt.show()