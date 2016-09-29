#!/usr/bin/env python
# Jiao Lin <jiao.lin@gmail.com>

def test_laz():
    from simbe import laz
    print laz.read("Fe.laz")
    return

def test():
    Fe = XSCalculator('Fe', 11.22, 0.4, 2.56)
    print Fe.xs(2200)
    lambdas = np.arange(0.5, 5.5, 0.1)
    xs = Fe.xs(lambdas)
    from matplotlib import pyplot as plt
    plt.plot(lambdas, xs)
    plt.show()
    return

if __name__ == '__main__': test_laz()

# End of file
