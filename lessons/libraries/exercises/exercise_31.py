from math import pi

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intg

x = np.arange(0, pi/2, 0.00001)
y = [np.sin(i) for i in x]

plt.plot(x, y, '.', color="blue", label="sin")
plt.show()

# riemann
riemann_integral = 0
for i in range(0, len(x)-1):
    if (y[i] > y[i+1]):
        b = y[i+1]
    else:
        b = y[i]
    riemann_integral += (x[i+1]-x[i])*b

print(riemann_integral)

# scipy
scipy_integral_ = intg.quad(lambda x: np.sin(x), 0, pi/2)

scipy_integral = scipy_integral_[0]

print(scipy_integral)
