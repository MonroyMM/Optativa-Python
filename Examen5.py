x=[41,41,71,70,35,46,3,11]
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

def masimetría(li=[]):
 nl=len(li)
 xm=media(li)
 var=varianza(li)

 sum=0
 for x in li:
  sum=sum+(x-xm)**3
   
 return (sum/nl)/(var**3)
 

print ('Asimetría: '+ str(masimetría([41,41,71,70,35,46,3,11])))


