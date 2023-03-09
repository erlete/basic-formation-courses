"""The implementation of the integrals is carried out in 2 ways:
    .1-Approach to the riemman sums by mean value of the base of the
        rectangle projecting its image(More efficient than
                                        avverage of the images of the ends
                                        of the rectangle).
    .2-Using scipy library.
"""
from time import perf_counter as pfc

import numpy as np
from scipy.integrate import quad

pi_mitad :float=np.divide(np.pi,2)
###############################################
# RIEMANN INTEGRAL
#  The idea is to use a born divisor of @pi_mitad to
#  achieve efficiency in the float representation(size interval).
#  We will permute the values in the middle of each interval,
#  this forces us to limit the final interval.
#  The error of riemman_integral is calculable,but it is not necessary in this scope.
#  [OPTIONAL]The use of fromiter is for a possible future update of numpy.1
start_riemann : 'float' = pfc()
riemann_paso :float = np.divide( pi_mitad ,120)#By hand but could be algorithmized
muestreo_x :float= np.arange( np.divide(riemann_paso,2) ,
                      pi_mitad - ( np.divide(riemann_paso , 4)) ,
                      riemann_paso)
riemann_integral :float = np.sum(np.fromiter( (np.sin(i)*riemann_paso for i in muestreo_x) ,
                                      float) )
end_riemann : 'float' = pfc()
###############################################
# SCIPY_INTEGRAL
#  We will create a helper function with which we will support
#  the quad module to calculate it.
##############################################
def f(x):
    return np.sin(x)
scipy_integral :float = quad( f , 0 , pi_mitad)[0]
end_scipy : 'float' = pfc()
##############################################
# TIME LIBRARY
#  We time the Start-End moments of the integrations
#  and substract them.
#  Multiply is MORE EFFICIENT on float(for that @end_riemmann*2)
##############################################
print( "Time Riemann_Integral - Time Scipy_Integral:" ,
      end_riemann *2  - start_riemann - end_scipy )
