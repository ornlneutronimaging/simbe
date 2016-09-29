# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>

import numpy as np
def read(path):
    converters = {
        0: int, 1: int, 2: int,
        }
    return np.loadtxt(path, converters=converters)

# End of file
