##############################################################################################
# Adding set of the modules important for this class
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
plt.switch_backend('Qt4Agg')
import matplotlib.patches as patches
import numpy as np
from PIL import Image

class CellDrawing(object):
    """Post processor for drawing the predictions of the output of the training
    (Updated 20/4/17)"""

    ###########################################################################################
    # Function for drawing the cells "Green" if it is predicted table "Blue" if it is Non-table
    # "Yellow" if its incorrectly predicted Non table and "Red" if its incorrectly predicted
    # Table
    def draw_prediction(self, arr, img, file_name):
        image = np.array(Image.open(img))
        fig, ax = plt.subplots(1)
        ax.imshow(image)
        for items in arr:
            # If it was predicted correctly table so green
            if (items.prediction == 1) and (items.table == 1):
                rect = patches.Rectangle((items.x, items.y),
                                     items.width, items.height,
                                     linewidth=1, edgecolor='g',
                                               facecolor='none')
                ax.add_patch(rect)
            # If it was predicted correctly non table so blue 
            elif(items.prediction == 0) and (items.table == 0):
                rect = patches.Rectangle((items.x, items.y),
                                     items.width, items.height,
                                     linewidth=1, edgecolor='b',
                                               facecolor='none')
                ax.add_patch(rect)
            # If it was predicted incorrectly table so red
            elif(items.prediction == 1) and (items.table == 0):
                rect = patches.Rectangle((items.x, items.y),
                                     items.width, items.height,
                                     linewidth=1, edgecolor='r',
                                               facecolor='none')
                ax.add_patch(rect)
            # If it was predicted incorrectly non-table so yellow
            elif(items.prediction == 0) and (items.table == 1):
                rect = patches.Rectangle((items.x, items.y),
                                     items.width, items.height,
                                     linewidth=1, edgecolor='y',
                                               facecolor='none')
                ax.add_patch(rect)
        plt.savefig(file_name + "_post_processor.png", transparent=True, dpi=300)
        plt.close()
        return

##############################################################################################
########################################END###################################################
##############################################################################################                       