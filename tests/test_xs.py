#!/usr/bin/env python
# Jiao Lin <jiao.lin@gmail.com>

import numpy as np
from simbe import laz, xscalc

def test_laz():
    print laz.read("Fe.laz")
    return

def test_xscalc():
    d = laz.read("Fe.laz")
    peaks = [
        xscalc.DiffrPeak(hkl, F, d, mult)
        for hkl, F, d, mult in zip(d['hkl'], d['F'], d['d'], d['mult'])
        ]
    Fe = xscalc.XSCalculator('Fe', 11.22, 0.4, 2.56, 2.886**3, peaks)
    print Fe.xs(2200)
    lambdas = np.arange(0.5, 5.5, 0.1)
    xs = [Fe.xs(l) for l in lambdas]
    from matplotlib import pyplot as plt
    plt.plot(lambdas, xs)
    plt.show()
    return

def test():
    # test_laz()
    test_xscalc()
    return

if __name__ == '__main__': test()

# End of file
