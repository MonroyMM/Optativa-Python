estructuras='''
ESTRUCTURAS CEREBRALES
1. Hipocampo
2. Amígdala
3. Tálamo
4. Hipotálamo
5. Cerebelo
'''
print(estructuras)

dd= dict()
dd['1']= "\nHipocampo\nEl hipocampo es una estructura alargada situada en la parte interna de los lóbulos temporales, una de las regiones de la corteza cerebral más antiguas, presentes en las formas de mamíferos más antiguas. Su función está relacionada con el almacenamiento y la recuperación de recuerdos, el aprendizaje y la navegación espacial."

dd['2']= "\nAmígdala\nLa amígdala cerebral forma parte del sistema límbico, y es una de las estructuras cerebrales que tienen más importancia a la hora de relacionar estados emocionales con situaciones que vivimos; es por eso que juega un papel clave en los procesos mentales relacionados con la memoria emocional y los aprendizajes vinculados a esta, que son muy importantes. A fin de cuentas, saber con qué emociones están emparejada cada tipo de estímulo o experiencia hace que adoptemos una actitud ante ellas y nos decantemos por unas posibles reacciones y no otras."

dd['3']= "\nTálamo\nEs el núcleo en el que se integra por primera vez toda la información que nos llega a través de los sentidos (a excepción del olfato, que llega al cerebro directamente a través del bulbo olfatorio de cada hemisferio cerebral). El tálamo manda esta información a áreas del cerebro más altas, para que allí se siga procesando la información que ha empezado a sintetizarse en él, y además es capaz de hacer posible que el Sistema Nervioso Autónomo reaccione rápidamente ante estímulos que pueden significar la presencia de un peligro."

dd['4']= "\nHipotálamo\nEl hipotálamo está situado justo debajo del tálamo, y se encarga principalmente de hacer que todo el organismo se encuentre constantemente en un estado de homeostasis, es decir, en equilibrio en todos los sentidos: temperatura corporal, niveles de hormonas en sangre, ritmo de la respiración, etc.También es la estructura responsable de la aparición del estado de sed y hambre."

dd['5']= "\nCerebelo\nEl cerebelo es una de las partes del cerebro con una mayor concentración de neuronas y entre sus muchas funciones la más estudiada es la regulación y monitorización de movimientos complejos que requieren una cierta coordinación. También tiene un papel en el mantenimiento del equilibrio al estar de pie y caminar."

def preg(ss=''):
 while True:
  res = input(ss)
  if res in dd:
   print(dd[res])
   return res

def preg2():
 while True:
  res = input('\n¿Te gustaría conocer alguna otra?\nS = Sí\nN = N\n')
  if res in ['S','N']:
   return res== 'S'
  


pregunta = '¿Cuál estructura cerebral te gustaría conocer? '

seguir=True
while seguir:
 res = preg(pregunta)
 seguir= preg2()
 if seguir:
  print(estructuras)


