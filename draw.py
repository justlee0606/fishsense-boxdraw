import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
from matplotlib.patches import Rectangle
import sys
from matplotlib.widgets import RectangleSelector

def main():

    def line_select_callback(eclick, erelease):

        """
        Callback for line selection.

        *eclick* and *erelease* are the press and release events.
        """
        coord[0], coord[1] = eclick.xdata, eclick.ydata
        coord[2], coord[3] = erelease.xdata, erelease.ydata

    def toggle_selector(event):
        if event.key == 't':
            if RS.active:
                print(f"TOP LEFT: ({coord[0]:3.2f}, {coord[1]:3.2f}) --> BOTTOM RIGHT: ({coord[2]:3.2f}, {coord[3]:3.2f})")
                print("Box confirmed. Press \'t\' to draw another box.")

                # Draw confirmed box
                rect = Rectangle((coord[0],coord[1]),coord[2]-coord[0],coord[3]-coord[1],linewidth=1,edgecolor='r',facecolor='none')
                ax.add_patch(rect)
                plt.draw()

                RS.set_active(False)
            else:
                print("Drawing mode activated.")
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
            "Press 't' to confirm box")
        coord = [0,0,0,0] # [x1, y1, x2, y2]
        RS = RectangleSelector(ax, line_select_callback,
                                            drawtype='box', useblit=True,
                                            button=[1],  # only draw using left click
                                            minspanx=5, minspany=5,
                                            rectprops=dict(edgecolor="red", alpha=1, fill=False),
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