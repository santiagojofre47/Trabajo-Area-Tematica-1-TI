#Ejercio 3

import struct
import math
import numpy as np

def CalcEntropia(nombre_archivo):
  frecuencia = np.zeros(256)
  entropia = 0
  with open(nombre_archivo, 'rb') as f: # Leemos el archivo como binario
      data = f.read()
      # Leemos los datos segun la estructura establecida
      for char in data:
        frecuencia[char] += 1
      for i in range(frecuencia.size):
        if frecuencia[i] != 0:
          prob = frecuencia[i]/len(data)
          entropia += prob*math.log2(1/prob)
  return str(entropia)

print("Entropia doc: " + CalcEntropia('test.doc'))
print("Entropia exe: " + CalcEntropia('test.exe'))
print("Entropia pdf: " + CalcEntropia('test.pdf'))
print("Entropia rar: " + CalcEntropia('test.rar'))
print("Entropia txt: " + CalcEntropia('test.txt'))
print("Entropia quijote: " + CalcEntropia('el_quijote.txt'))
