import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
from matplotlib.widgets import RectangleSelector
from user_control import line_select_callback, toggle_selector

# Get paths to RGB and depth image
try:
    rgb_img_str = str(sys.argv[1])
    depth_img_str = str(sys.argv[2])
except:
    print("RGB and depth images needed")
    exit()

# Start drawing
try:
    # Open RGB image
    rgb_img = mpimg.imread(rgb_img_str)

    fig, ax = plt.subplots()
    ax.set_title(
        "Click and drag to draw a rectangle.\n"
        "Press 't' to toggle the selector on and off.")
    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                        drawtype='box', useblit=True,
                                        button=[1, 3],  # disable middle button
                                        minspanx=5, minspany=5,
                                        spancoords='pixels',
                                        interactive=True)
    fig.canvas.mpl_connect('key_press_event', toggle_selector)

    imgplot = plt.imshow(rgb_img)
    plt.show()
except:
    print("Path not correct or image not found")
    exit()

print("Finished!")