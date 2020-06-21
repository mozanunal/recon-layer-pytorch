
from torch import nn

class ForwardProj(nn.Module):
    def __init__(self, geo, out_size):
        super(ForwardProj, self).__init__()
        self.geo = geo
        self.out_size

    def _systemMatrix(self, ):
        pass


    def _projMatrix(self, angle):
        # cur_source_pos = 
        # cur_det_pos = 
        pass

    def forward(self, x, angles):
        
        return x


