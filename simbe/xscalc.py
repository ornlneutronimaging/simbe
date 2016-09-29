# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>

import numpy as np
from numpy import pi

class XSCalculator:

    def __init__(
        self, name, coh_xs, inc_xs, abs_xs_at2200,
        diffpeaks
    ):
        self.name = name
        self.coh_xs = coh_xs
        self.inc_xs = inc_xs
        self.abs_xs_at2200 = abs_xs_at2200
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
        return 0

    def xs_abs(self, wavelen):
        Q = 2*pi/wavelen
        from mcni.utils.conversion import K2V
        v = K2V*Q
        return self.abs_xs_at2200/v*2200


def test():
    Fe = XSCalculator('Fe', 11.22, 0.4, 2.56)
    print Fe.xs(2200)
    lambdas = np.arange(0.5, 5.5, 0.1)
    xs = Fe.xs(lambdas)
    from matplotlib import pyplot as plt
    plt.plot(lambdas, xs)
    plt.show()
    return


if __name__ == '__main__': test()


# End of file
