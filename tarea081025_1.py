import matplotlib.pyplot as plt
import numpy as np

h=0.01

x= np.arange(-1,4,h)

y = []


for i in np.arange(len(x)):
    y2= x[i]**2
    y.append(y2)

y = y[:]

xt = np.arange(-1,4,h)
yt = []

for ss in np.arange(len(xt)):
    y3= 2*xt[ss]-1
    yt.append(y3)

yt = yt[:]

plt.plot(x,y)
plt.plot(xt,yt,'r')
plt.show()