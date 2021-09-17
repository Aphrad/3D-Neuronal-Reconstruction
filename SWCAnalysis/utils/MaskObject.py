import numpy as np
from utils import params
import matplotlib.pyplot as plt


class MaskObject:
    def __init__(self, maskPath, *, fromPath=True, preserveSID=True, preserveRadius=True):
        """
        todo
        Params:	swcPath - string, absolute path of swc file
            fromPath - boolean, if true reads swc from file, else reads from array
            swcArray - 2d numpy arraym
            preserveSID - boolean, if false will set all structure id values to 0
            preserveRadius - boolean, if false will set all radius values to 0

        This constructor only calls loadSWCFile() to get the swcArray
        that will be used to represent the SWC
        """
        self.filename = maskPath
        self.loadMaskFile()

    def loadMaskFile(self):
        print('Loading MaskFilename:', self.filename.split('/')[-1])
        self.swcArray = np.load(self.filename)["arr_0"]

    def concat(self, obj1, obj2, dim):
        pass
    
    def plot(self, savepath = None):
        dimension = self.swcArray.ndim

        # 2D part
        # todo
        if dimension == 2:
            pass
        elif dimension == 3:
            fig = plt.figure(figsize=(4, 4), dpi=100)
            ax = fig.add_subplot(111, projection='3d')
            position_list = np.argwhere(self.swcArray == 1)
            pos_x = [position[2] for position in position_list]
            pos_y = [-position[1] for position in position_list]
            pos_z = [position[0] for position in position_list]
            ax.scatter(xs=pos_x, ys= pos_y,
                       zs=pos_z,
                       color=params.SOMA_DEFAULT_COLOR, s=params.SOMA_DEFAULT_RADIUS)

            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
            plt.margins(0, 0, 0)
            plt.axis('off')
            plt.show()
            if savepath is not None:
                fig.savefig(savepath, dpi=300)


if __name__ == "__main__":
    MaskFilename = '../dataset/lbl_1_0_1_3.npz'
    Mask = MaskObject(MaskFilename)
    Mask.plot(savepath= '../result/mask_1_0_1_3.png')