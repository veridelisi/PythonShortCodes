# http://www.financialexamhelp123.com/par-curve-spot-curve-and-forward-curve/
# Alexander Baker, March 2012 Yield Curve Bootstrapper


from sympy import Symbol, solve, Abs

x = Symbol('x', real=True)

def g(yieldCurve, zeroRates, n, verbose):
    if len(zeroRates) >= len(yieldCurve):
        print("\n\n\t+zero curve bootstrapped [%d iterations]" % (n))
        return
    else:
        legn = ''
        for i in range(0, len(zeroRates), 1):
            if i == 0:
                legn = '%2.6f/(1+%2.6f)**%d' % (yieldCurve[n], zeroRates[i], i + 1)
            else:
                legn = legn + ' +%2.6f/(1+%2.6f)**%d' % (yieldCurve[n], zeroRates[i], i + 1)
        legn = legn + '+ (1+%2.6f)/(1+x)**%d-1' % (yieldCurve[n], n + 1)

        if verbose:
            print("-[%d] %s" % (n, legn.strip()))

        rate1 = solve(eval(legn), x)
        rate1 = min([Abs(r) for r in rate1])

        if verbose:
            print("-[%d] solution %2.6f" % (n, float(rate1)))

        zeroRates.append(rate1)
        g(yieldCurve, zeroRates, n + 1, verbose)

verbose = True
tenors = [0.5, 1, 1.5, 2, 2.5, 3]

yieldCurve = [0.02, 0.024, 0.0276, 0.030840, 0.033756, 0.036380]

zeroRates = [yieldCurve[0]]

print("\n\n\tAlexander Baker, March 2012\n\tYield Curve Bootstrapper\n\tAlexander Baker\n\n")

g(yieldCurve, zeroRates, 1, verbose)
print("\tZeroRate Array", zeroRates)

pylab.plot(tenors, yieldCurve)
pylab.plot(tenors, zeroRates)
pylab.show()
