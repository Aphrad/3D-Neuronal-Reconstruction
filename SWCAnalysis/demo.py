from utils import SWCObject

if __name__ == "__main__":
    SWCFilename = 'dataset/test_1.swc'
    SWC = SWCObject(SWCFilename)
    SWC.plot(dim=3, savepath= 'result/test_1.png')
