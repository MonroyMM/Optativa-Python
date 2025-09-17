x=[10, 2, 38, 23, 38, 23, 21, 23]
print('Dados: ')
print('x= '+ str(x))

def media(li=[]):
 nl=len(li)
 sum=0

 for x in li:
  sum=sum+x

 return sum/nl

def varianza(li=[]):
 nl=len(li)
 xm=media(li)

 sum=0
 for x in li:
  sum=sum+(x-xm)**2
   
 return sum/(nl-1)

def kurtosis(li=[]):
 nl=len(li)
 xm=media(li)
 var=varianza(li)

 sum=0
 for x in li:
  sum=sum+(x-xm)**4
   
 return ((sum/nl)/(var**4))-3
 

print ('Kurtosis: '+ str(kurtosis([10, 2, 38, 23, 38, 23, 21, 23])))
