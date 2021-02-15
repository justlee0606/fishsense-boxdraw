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
        rgb_coord[0], rgb_coord[1] = eclick.xdata, eclick.ydata
        rgb_coord[2], rgb_coord[3] = erelease.xdata, erelease.ydata
        depth_coord[0], depth_coord[1] = rgb_coord[0]*scale_w, rgb_coord[1]*scale_h
        depth_coord[2], depth_coord[3] = rgb_coord[2]*scale_w, rgb_coord[3]*scale_h


    #def saveCoords():

    def toggle_selector(event):
        if event.key == 't':
            if RS.active:
                if sum(rgb_coord) == 0:
                    print("No box detected. Please draw a box.")
                else:
                    print(f"RGB IMAGE: \n TOP LEFT: ({rgb_coord[0]:3.2f}, {rgb_coord[1]:3.2f}) --> BOTTOM RIGHT: ({rgb_coord[2]:3.2f}, {rgb_coord[3]:3.2f})")
                    print(f"DEPTH IMAGE: \n TOP LEFT: ({depth_coord[0]:3.2f}, {depth_coord[1]:3.2f}) --> BOTTOM RIGHT: ({depth_coord[2]:3.2f}, {depth_coord[3]:3.2f})")
                    print("Box confirmed. Press \'t\' to draw another box.")

                    # Draw confirmed box
                    rect = Rectangle((rgb_coord[0],rgb_coord[1]),rgb_coord[2]-rgb_coord[0],rgb_coord[3]-rgb_coord[1],linewidth=1,edgecolor='r',facecolor='none')
                    ax.add_patch(rect)
                    plt.draw()

                    saveCoords()

                    #Reset coordinates and deactivate draw mode
                    for i in range(4): rgb_coord[i] = 0
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

        # Get image dimensions and scale
        rgb_h, rgb_w = rgb_img.shape[0], rgb_img.shape[1]
        depth_h, depth_w = depth_img.shape[0], depth_img.shape[1]
        scale_h, scale_w = depth_h/rgb_h, depth_w/rgb_w

        print(scale_h)
        print(scale_w)

        fig, ax = plt.subplots()
        ax.set_title(
            "Click and drag to draw a rectangle.\n"
            "Press 't' to confirm box")
        rgb_coord = [0,0,0,0] # [x1, y1, x2, y2]
        depth_coord = [0,0,0,0]
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