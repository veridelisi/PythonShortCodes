#https://analystprep.com/study-notes/cfa-level-2/describe-how-zero-coupon-rates-spot-rates-may-be-obtained-from-the-par-curve-by-bootstrapping/
'''
Annual Par-Rates
Year  Par Rate  Zero-coupon rate (Implied Spot rate)
1     2.00      2.00
2     2.60      2.61
3     2.90      2.91
4     3.80      3.87
'''


# r(2) 
# \begin{align*} 1 &=\frac{0.026}{1.02}+\frac{(1+0.026)}{\left(1+r\left(2\right)\right)^2} \\ r (2) & =2.61\% \end{align*}

from scipy.optimize import fsolve
import numpy as np

# Define the equation as a function
def equation(r):
    return 0.026 / 1.02 + 1.026 / (1 + r)**2 - 1

# Use fsolve to find the root (r(2))
r_2 = fsolve(equation, 0.026)
r_2_percentage = r_2 * 100  # Convert to percentage

print(r_2_percentage)


# r(3) 
# \begin{align*} 1 &=\frac{0.029}{1.02}+\frac{0.029}{{1.0261}^2}+\frac{1.029}{\left(1+r\left(3\right)\right)^3} \\ r (3) & = 2.91\% \end{align*}

from scipy.optimize import fsolve

# Define the equation as a function
def equation(r):
    return 0.029 / 1.02 + 0.029 / (1.0261**2) + 1.029 / (1 + r)**3 - 1

# Use fsolve to find the root (r(3))
r_3 = fsolve(equation, 0.029)
r_3_percentage = r_3 * 100  # Convert to percentage

print(r_3_percentage)

# r(4) 
# \begin{align*} 1 &=\frac{0.038}{1.02}+\frac{0.038}{{1.0261}^2}+\frac{0.038}{{1.0291}^3}+\frac{1.038}{\left(1+r\left(4\right)\right)^4} \\ r (4) & = 3.87\% \end{align*}

from scipy.optimize import fsolve

# Define the equation as a function
def equation(r):
    return 0.038 / 1.02 + 0.038 / (1.0261**2) + 0.038 / (1.0291**3) + 1.038 / (1 + r)**4 - 1

# Use fsolve to find the root (r(4))
r_4 = fsolve(equation, 0.038)
r_4_percentage = r_4 * 100  # Convert to percentage

print(r_4_percentage)

#\begin{array}{c|c|c} \textbf{Year} & \textbf{Par Rate} & \textbf{Zero-coupon rate} \\ & & \textbf{(Implied Spot rate)} \\ \hline 1 & 2.00\% & 2.00\% \\ \hline 2 & 2.60\% & 2.61\% \\ \hline 3 & 2.90\% & 2.91\% \\ \hline 4 & 3.80\% & 3.87\% \end{array}
