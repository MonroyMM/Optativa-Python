fillin=open('texto_tarea.txt', 'r')

datos= fillin.read()
print(type(datos))

lineas=datos.split('\n')

for palabra in list(lineas):
 if ('Corrieron ' in palabra):
  lineas.remove(palabra)

for palabra in list(lineas):
 if ('.- ' in palabra):
  print(palabra)

