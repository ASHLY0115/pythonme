from matplotlib import pyplot as plt
import numpy as np
import math
#plot1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(3,3,1)
plt.plot(x,y)

#plot 2
x=np.array([0,1,2,3])
y=np.array([20,10,30,40])
plt.subplot(3,3,2)
plt.plot(x,y)

#plot 3
x=[1,2,3,4,4,3,3,6,6,8,8,8,8,8,1,1,1,2,24,6,8]
plt.subplot(3,3,3)
plt.hist(x)
plt.show()

#plot 4
x=np.array([0,1,2,3])
y=np.array([20,10,30,40])
plt.subplot(3,3,4)
plt.plot(x,y)


plt.show()
