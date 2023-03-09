import matplotlib.pyplot as plt
import numpy as np
import scipy
#SE PUEDE HACER EN UN BUCLE O(1) SABIENDO MANEJAR PUNTEROS
#EN PYTHON lo cual tendría que fuchicar la de dios
#y quedan 30 min
img = scipy.datasets.face()  # Sample image
def splitter(img):
   toret=[[],[],[]]
   mascara=np.array([[0xFF,0x0,0x0],[0x0,0xFF,0x0],[0x0,0x00,0xFF]])
   for i in img:#¿Se puede hacer en 1 Bucle(típico java)?si,pero menos eficiente,es mas eficiente el bucle de 3 después
      for x in range(0,3):#Mantengo la idea hasta la muerte
         toret[x].append([z[x] & mascara[x] for z in i])
   #Ahora con un método tener la img original es O(1),pero no me sé los parámetros
   for x in toret:
      x=np.array(x)
   return toret
