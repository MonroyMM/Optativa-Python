n=1456
print('Dado: ' + str(n))

binario=''

if n== 0:
 binario= binario + '0'
else:
 while n>0:
  res=n%2
  binario= binario + str(res)
  n=n//2

binario_rev=list(reversed(binario))
print(binario_rev)

binario_r=''.join(reversed(binario))
print('Binario: '+ binario_r)