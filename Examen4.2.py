ss='100110011000'
sum=0
el=0

for i in reversed(ss):
 if i == '1':
  sum=sum+(2**el)
  el=el+1
 else:
  el=el+1
 

print('Dado:'+ ss)
print('Número decimal: '+ str(sum))