from matplotlib import pyplot as plt
import numpy as np
import math
x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("angles")
plt.ylabel("values")
plt.subplot(2,1,1)

x=np.arange(0,math.pi*2,0.05)
y=np.cos(x)
plt.plot(x,y)
plt.xlabel("angles")
plt.ylabel("values")
plt.subplot(2,1,2)

plt.show()