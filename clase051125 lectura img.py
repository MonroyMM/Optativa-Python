import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_path = 'frame0001.png'

image = mpimg.imread(image_path)

print(type(image))

vol =image[:,:, 0]
subregion =vol[750:1000,240:560]

min = np.min(subregion)
max = np.max(subregion)

print(min)
print(max)

min2 = np.min(image)
max2 = np.max(image)

print(min2)
print(max2)


x= 1
minimos=[]
maximos=[]

while x <= 631: 
 if x < 10:
  image_path = 'frame000'+str(x)+'.png'
 elif x < 100:
  image_path = 'frame00'+str(x)+'.png'
 else:
  image_path = 'frame0'+str(x)+'.png'

 image = mpimg.imread(image_path)
 min = np.min(image)
 max = np.max(image)
 minimos.append(float(min))
 maximos.append(float(max))
 x=x+1
   

#print(minimos)
#print(maximos)


print(image.shape)
plt.imshow(subregion)
plt.show()

plt.plot(minimos, maximos)
plt.plot(minimos, 'r')
plt.plot(maximos, 'b')
plt.show()