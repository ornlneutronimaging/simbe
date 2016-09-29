# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>

import numpy as np
def read(path):
    data = np.loadtxt(path)
    # H  K  L  THETA  2THETA D VALUE  1/D**2 SIN2*1000  H  K  L INTENSITY         /F(HKL)/       A(HKL)      B(HKL) PHA.ANG. MULT   LPG
    return dict(
        hkl = np.array(data[:, :3], dtype=int),
        theta = data[:, 3],
        d = data[:, 5],
        mult = np.array(data[:, 16], dtype=int),
        F = data[:, 12],
        )

# End of file
