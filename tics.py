import matplotlib.pyplot as plt
import random
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y= [random.randint(1,10) for i in range(15)]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y)
plt.show()