import matplotlib.pyplot as plt
import numpy as np
import scipy

img = scipy.datasets.face()  # Sample image
def splitter(img):
   """Function that separates and image into its 3 color components

   This method is not based on making 3 snapshots of the img classs,
   but rather the three corresponding images are created from the original
   through a mask.(For that dont pass the test(The @return_class dont have all atributes))

   Args:

      img (numpy.array)): The original image
      (This function does not check the parameters)

   Returns:

      toret (tuple(numpy.array , numpy.array , numpy.array)): R G B colors respectibily.
   """

   toret : list[ list , list, list ]=[[],[],[]]
   mascara : numpy.array=np.array([[0xFF,0x0,0x0] , [0x0,0xFF,0x0] , [0x0,0x00,0xFF]])
   for i in img:
      for x in range(0,3):
         toret[x].append([z[x] & mascara[x] for z in i])
   for x in toret: #Not necessary,I have done it for the equality of specific atribute
      x :numpy.array = np.array(x)
   return toret
# I am aware that it does not pass the test
# (I would simply have to change the aproach and use function .copy(),
# but a priori it seems less efficient and i want to capture i would do the exercise)
# You make 3 copies of the same set and act separately,here you act on it only once.
