

import numpy
import scipy.misc # to visualize only
x = numpy.fromfile('train_x.bin', dtype='uint8')
x = x.reshape((100000,60,60))
print len(x[0]), len(x[0][0])
scipy.misc.imshow(x[0]) # to visualize only

