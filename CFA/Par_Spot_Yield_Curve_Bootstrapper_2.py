#http://www.financialexamhelp123.com/par-curve-spot-curve-and-forward-curve/
#mastering-python-for-finance-second-edition

def zero_coupon_bond(par, y, t):
    """
    Price a zero coupon bond.
    
    :param par: face value of the bond.
    :param y: annual yield or rate of the bond.
    :param t: time to maturity, in years.
    """
    return par/(1+y)**t

print(zero_coupon_bond(100, 0.02, 0.5))
print(zero_coupon_bond(100, 0.024, 1))
print(zero_coupon_bond(100, 0.0276, 1.5))
print(zero_coupon_bond(100, 0.030840, 2))
print(zero_coupon_bond(100, 0.033756, 2.5))
print(zero_coupon_bond(100, 0.036380, 3))

"""
99.01475429766742
97.65625
95.99836946727454
94.10603498524202
92.03539739675895
89.83445342308401

"""

import math

class BootstrapYieldCurve(object):    
    
    def __init__(self):
        self.zero_rates = dict()
        self.instruments = dict()
        
    def add_instrument(self, par, T, coup, price, compounding_freq=2):
        self.instruments[T] = (par, coup, price, compounding_freq)
    
    def get_maturities(self):
        """ 
        :return: a list of maturities of added instruments 
        """
        return sorted(self.instruments.keys())
    
    def get_zero_rates(self):
        """ 
        Returns a list of spot rates on the yield curve.
        """
        self.bootstrap_zero_coupons()    
        self.get_bond_spot_rates()
        return [self.zero_rates[T] for T in self.get_maturities()]    
        
    def bootstrap_zero_coupons(self):
        """ 
        Bootstrap the yield curve with zero coupon instruments first.
        """
        for (T, instrument) in self.instruments.items():
            (par, coup, price, freq) = instrument
            if coup == 0:
                spot_rate = self.zero_coupon_spot_rate(par, price, T)
                self.zero_rates[T] = spot_rate        
                
    def zero_coupon_spot_rate(self, par, price, T):
        """ 
        :return: the zero coupon spot rate with continuous compounding.
        """
        spot_rate = math.log(par/price)/T
        return spot_rate
                    
    def get_bond_spot_rates(self):
        """ 
        Get spot rates implied by bonds, using short-term instruments.
        """
        for T in self.get_maturities():
            instrument = self.instruments[T]
            (par, coup, price, freq) = instrument
            if coup != 0:
                spot_rate = self.calculate_bond_spot_rate(T, instrument)
                self.zero_rates[T] = spot_rate
                
    def calculate_bond_spot_rate(self, T, instrument):
        try:
            (par, coup, price, freq) = instrument
            periods = T*freq
            value = price
            per_coupon = coup/freq
            for i in range(int(periods)-1):
                t = (i+1)/float(freq)
                spot_rate = self.zero_rates[t]
                discounted_coupon = per_coupon*math.exp(-spot_rate*t)
                value -= discounted_coupon

            last_period = int(periods)/float(freq)        
            spot_rate = -math.log(value/(par+per_coupon))/last_period
            return spot_rate
        except:
            print("Error: spot rate not found for T=", t)


yield_curve = BootstrapYieldCurve()
yield_curve.add_instrument(100, 0.5, 0.02, 99.01475429766742,2)
yield_curve.add_instrument(100, 1.0, 0.024, 97.65625,2  )
yield_curve.add_instrument(100, 1.5, 0.0276, 95.99836946727454,2  )
yield_curve.add_instrument(100, 2.0, 0.030840, 94.10603498524202,2  )
yield_curve.add_instrument(100, 2.5, 0.033756, 92.03539739675895,2  )
yield_curve.add_instrument(100, 3.0, 0.036380, 89.83445342308401,2  )


y = yield_curve.get_zero_rates()
x = yield_curve.get_maturities()


%pylab inline

fig = plt.figure(figsize=(12, 8))
plot(x, y)
title("Zero Curve") 
ylabel("Zero Rate (%)")
xlabel("Maturity in Years");

