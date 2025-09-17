ni=1000
del1=(3+1)/ni
area=0
print('Para la derivada: \n')
print('f(x)=(4-(x-1)**2)\n')
print('En el intervalo (-1,3)\n')

x=-1

for i in range(ni+1):
 area=area+del1*(4-(x-1))**2
 x=x+del1

print('El área corresponde a: '+ str(area))

