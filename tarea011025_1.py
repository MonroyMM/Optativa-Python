import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-6, 6, 0.001)
a=1
b=49
c= 0

x = np.cos(a*t) + ((np.cos(b*t))/2) + ((np.sin(c*t))/3)
y = np.sin(a*t) + ((np.sin(b*t))/2) + ((np.cos(c*t))/3)

plt.plot(x,y)

plt.show()
plt.close()