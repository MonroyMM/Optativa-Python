import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((256, 256))

lineas = 20

for ss in range(lineas):
    b = np.random.uniform(0, 256)
    m = np.random.uniform(-5, 5)
    x = np.arange(0, 256)
    y = m * x + b
    for j in range(len(x)):
        corx = int(x[j])
        cory = int(y[j])
        if 0 <= corx < 256 and 0 <= cory < 256:
            img[cory, corx] = 255

plt.imshow(img)
plt.show()