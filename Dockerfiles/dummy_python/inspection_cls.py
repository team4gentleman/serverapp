import numpy as np

class Inspection():
    def execute(self, imgfile, modelfile='model', meanfile='mean.npy'):
        ret = np.array([('normal', 0.20466148853302002), ('hengao', 0.1924593597650528), ('excellent', 0.07535989582538605), ('bad', 0.07535989582538605), ('drunker', 0.07535989582538605), ('hd', 0.07535989582538605)])
        return ret

    if __name__ == "__main__":
        print execute('/var/opt/t4j/chainer-data/tmpimages/image0000000.jpg')
