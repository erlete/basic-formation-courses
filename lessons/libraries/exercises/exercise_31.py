import numpy as np
from scipy.integrate import quad

pi_mitad=np.divide(np.pi,2)#0.2 tiene mismo patron division que 2(pi/2)tendremos que sumar algo para ejecutar el final
riemann_paso=0.0001
muestreo_x=np.arange(np.divide(riemann_paso,2),pi_mitad-(np.divide(riemann_paso,4)),riemann_paso)#Integración numérica valor intermedio a 2 puntos por eso resto 0.1,para no hacer un suma de más.
riemann_integral=np.sum((np.sin(i)*riemann_paso for i in muestreo_x))
def f(x):
    return np.sin(x)
scipy_integral=quad(f,0,pi_mitad)[0]
