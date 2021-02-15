import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import numpy as np
import sys
from matplotlib.widgets import RectangleSelector

def main():

    def line_select_callback(eclick, erelease):
        """
        Callback for line selection.

        *eclick* and *erelease* are the press and release events.
        """
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")

    def toggle_selector(event):
        if event.key == 't':
            if RS.active:
                print(' RectangleSelector deactivated.')
                RS.set_active(False)
            else:
                print(' RectangleSelector activated.')
                RS.set_active(True)

    # Get paths to RGB and depth image
    try:
        rgb_img_str = "images/" + str(sys.argv[1])
        depth_img_str = "images/" + str(sys.argv[2])
    except:
        print("RGB and depth images needed")
        exit()

    # Start drawing
    try:

        #Disable toolbar on UI
        mpl.rcParams['toolbar'] = 'None'

        # Open RGB image
        rgb_img = mpimg.imread(rgb_img_str)
        depth_img = mpimg.imread(depth_img_str)

        fig, ax = plt.subplots()
        ax.set_title(
            "Click and drag to draw a rectangle.\n"
            "Press 't' to toggle the selector on and off.")
        # drawtype is 'box' or 'line' or 'none'
        RS = RectangleSelector(ax, line_select_callback,
                                            drawtype='box', useblit=True,
                                            button=[1],  # only draw using left click
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

if __name__ == "__main__":
    main()