import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
from matplotlib.widgets import RectangleSelector

# Get paths to RGB and depth image
try:
    rgb_img_str = str(sys.argv[1])
    depth_img_str = str(sys.argv[2])
except:
    print("RGB and depth images needed")
    exit()

# Open RGB image
try:
    rgb_img = mpimg.imread(rgb_img_str)
    imgplot = plt.imshow(rgb_img)
    plt.show()
except:
    print("Path not correct or image not found")
    exit()

print("Finished!")