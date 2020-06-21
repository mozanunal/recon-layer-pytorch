
import matplotlib.pyplot as plt
import numpy as np


"""
1 projection
 y =     A      x
(m,1) = (m,n) x (n,1)

n = img_res0 x img_res1
m = det_res0
"""

class Geo2d(object):
    def __init__(self,
        source_position = (0.0, 6.0),
        img_mid_pos = (0.0, 0.0),
        img_size = (6.0, 6.0),
        img_res = (200, 200),
        det_mid_pos = (0.0, -6.0),
        det_size = (15,),
        det_res = (400),
        ):
        self.source_position = np.array( source_position )
        self.img_mid_pos = np.array( img_mid_pos )
        self.img_size = np.array( img_size )
        self.img_res = np.array( img_res )
        self.det_mid_pos = np.array( det_mid_pos )
        self.det_size = np.array( det_size )
        self.det_res = np.array( det_res )

    def plot(self):
        plt.figure()
        currentAxis = plt.gca()
        # source plot
        plt.scatter(x=self.source_position[0],
                    y=self.source_position[1], 
                    s=40, marker="*")
        # detector plot
        x = np.linspace(self.det_mid_pos[0] - self.det_size[0]/2, 
                        self.det_mid_pos[0] + self.det_size[0]/2)
        y = np.linspace(self.det_mid_pos[1], self.det_mid_pos[1])
        plt.plot(x,y, marker='<')
        # img plot
        corner_poss = (self.img_mid_pos[0]-self.img_size[0]/2, 
                       self.img_mid_pos[1]-self.img_size[1]/2 )
        rect = plt.Rectangle(corner_poss, self.img_size[0], self.img_size[1])
        currentAxis.add_patch(rect)
        currentAxis.axis('equal')
        plt.show()


class Geo3d(object):
    def __init__(self):
        pass


#
#      * source (0,6)
#      | 3cm 
#    -----
#   |     | object
#   |     |  (0,0) 6x6
#    -----
#      | 3cm
# ------------- (0,-6) 15
example_geo = Geo2d( )