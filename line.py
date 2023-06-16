from matplotlib import pyplot as plt
import numpy as np
import math
t=np.arange(0.,4.,0.2)
plt.plot(t,t,'r--',t,t**2,'g+',t,t**3,'y^',)
plt.ylabel("some numbers")
plt.show()