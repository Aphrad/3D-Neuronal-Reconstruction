import numpy as np
from utils import params
import matplotlib.pyplot as plt

class SWCObject:
    def __init__(self, swcPath, *, fromPath=True, swcArray=None, preserveSID=True, preserveRadius=True):
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
        self.filename = swcPath
        self.loadSWCFile()

    def loadSWCFile(self):
        print('Building SWCFilename:', self.filename.split('/')[-1])
        self.swcArray = np.genfromtxt(self.filename, delimiter=params.SWC_DELIMITER, dtype=object).astype("float64")

    def plot(self, dim, savepath = None):
        uniqueSID = np.unique(self.swcArray[:, params.SWC_INDICES["sid"]])

        # 2D part
        # todo
        if dim == 2:
            pass
            """
            for sid in uniqueSID:
                sidCoords = self.swcArray[self.swcArray[:, params.SWC_INDICES["sid"]] == sid]
                plt.scatter(sidCoords[:, params.SWC_INDICES["x"]], -sidCoords[:, params.SWC_INDICES["y"]],
                            color=params.SID_COLORS[sid], s=params.SID_PLOTTING_RADII[sid])
            plt.show()
            """
        elif dim == 3:
            fig = plt.figure(figsize=(8, 8), dpi=100)
            ax = fig.add_subplot(111, projection='3d')
            for sid in uniqueSID:
                sidCoords = self.swcArray[self.swcArray[:, params.SWC_INDICES["sid"]] == sid]
                ax.scatter(xs=sidCoords[:, params.SWC_INDICES["x"]], ys=-sidCoords[:, params.SWC_INDICES["y"]],
                           zs=sidCoords[:, params.SWC_INDICES["z"]],
                           color=params.SID_COLORS[sid], s=sidCoords[:, params.SWC_INDICES["radius"]])

            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
            plt.margins(0, 0, 0)
            plt.axis('off')
            plt.show()
            if savepath is not None:
                fig.savefig(savepath, dpi = 300)

if __name__ == "__main__":
    SWCFilename = '../dataset/test_1.swc'
    SWC = SWCObject(SWCFilename)
    SWC.plot(dim=3, savepath= '../result/test_1.png')