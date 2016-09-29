# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>

import numpy as np
from numpy import pi

class XSCalculator:

    def __init__(
        self, name, coh_xs, inc_xs, abs_xs_at2200,
        uc_vol,
        diffpeaks
    ):
        self.name = name
        self.coh_xs = coh_xs
        self.inc_xs = inc_xs
        self.abs_xs_at2200 = abs_xs_at2200
        self.uc_vol = uc_vol
        self.diffpeaks = diffpeaks
        return

    def xs(self, wavelen):
        """wavelen: angstom
        """
        abs = self.xs_abs(wavelen)
        coh = self.xs_coh(wavelen)
        inc = self.xs_inc(wavelen)
        return abs+coh+inc

    def xs_inc(self, wavelen):
        return 0

    def xs_coh(self, wavelen):
        vs = [np.abs(p.F)**2*p.d*p.mult for p in self.diffpeaks if p.d*2>wavelen]
        return np.sum(vs) * wavelen*wavelen/(2*self.uc_vol)

    def xs_abs(self, wavelen):
        Q = 2*pi/wavelen
        from mcni.utils.conversion import K2V
        v = K2V*Q
        return self.abs_xs_at2200/v*2200


class DiffrPeak:
    
    def __init__(self, hkl, F, d, mult):
        self.hkl = hkl
        self.F = F
        self.d = d
        self.mult = mult
        return


if __name__ == '__main__': test()


# End of file
