d1='''
<!DOCTYPE html>
 <html>
 <head>
  <title>Clase Python</title>
 </head>
 <body>
'''

d2='''
 </body>
</html>
'''

li=["(Bouton, 1988) Context and ambiguity in the extinction of emotional learning.pdf", "(Delamater, 2004) Experimental extinction in Pavlovian conditioning behavioural and neuroscience perspectives.pdf", "(Halladay et al., 2012) Reinstatement of extinguishe fear by an unextinguished conditional stimulus.pdf", "(King et al., 2018) Individual differences in fear relapse.pdf", "(Maren, 2016) Stress and Fear Extinction.pdf", "(Milad) Fear extinction -book-.pdf", "(Quirk, 2008) Neural Mechanisms of Extinction Learning and Retrieval.pdf", "(Rescorla, 2004) Spontaneous Recovery.pdf", "+ (Gershman, 2010). Context, learning, and extinction.pdf", "+ (Heald, 2023) Contextual inference in learning and memory.pdf", "+(Bouton et al., 2021) Behavioral-and-neurobiological-mechanisms-of-pavlovian-and-instrumental-extinction-learning.pdf"]


filo=open('ejem.html', 'w')

filo.write(d1)


for ss in li:
 v1= '<p> <a href="C:/Users/Mónica Monroy/OneDrive/Desktop/Extinción/'+ ss + '"> Artículo </a> </p>'
 filo.write(v1)

filo.write(d2)
filo.close()
