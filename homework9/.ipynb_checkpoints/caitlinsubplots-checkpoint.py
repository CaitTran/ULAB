import numpy as np
import matplotlib.pyplot as plt

def horizontal_subplots(any_x):
    """
    Input: an x array/list
    Output: 2 subplots of cos(x) and sin(x) placed horizontally next to each other
    """
    
    #create the subplots figure (1 row, 2 columns)
    fig, ax = plt.subplots(1, 2, figsize = (10, 10))
    plt.subplots_adjust(wspace = 0.5)

    #create the y-values for both functions
    y_1 = np.cos(any_x)
    y_2 = np.sin(any_x)

    #function 1: h(x)
    ax[0].plot(any_x, y_1, label = "h(x) = cos(x)")
    ax[0].set_title("h(x) = cos(x)")
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")

    #function 2: g(x)
    ax[1].plot(any_x, y_2, label = "g(x) = sin(x)")
    ax[1].set_title("g(x) = sin(x)")
    ax[1].set_xlabel("X-axis")
    ax[1].set_ylabel("Y-axis")

    
def vertical_subplots(any_x):
     """
    Input: an x array/list
    Output: 2 subplots of cos(x) and sin(x) stacked vertically
    """
    
    #create the subplots figure (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize = (10, 10))
    plt.subplots_adjust(wspace = 0.5)

    #create the y-values for both functions
    y_1 = np.cos(any_x)
    y_2 = np.sin(any_x)

    #function 1: h(x)
    ax[0].plot(any_x, y_1, label = "h(x) = cos(x)")
    ax[0].set_title("h(x) = cos(x)")
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")

    #function 2: g(x)
    ax[1].plot(any_x, y_2, label = "g(x) = sin(x)")
    ax[1].set_title("g(x) = sin(x)")
    ax[1].set_xlabel("X-axis")
    ax[1].set_ylabel("Y-axis")

        