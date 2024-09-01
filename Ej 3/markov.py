import struct
import math
import numpy as np



def CalcEntropia(nombre_archivo):
  frecuencia = np.zeros((256, 256), dtype=float)
  frecuencia.fill(0.001)
  entropia = 0
  lista:list[bytes] = []
  with open(nombre_archivo, 'rb') as f: # Leemos el archivo como binario
      data = f.read()
      # Leemos los datos segun la estructura establecida
      for char in data:
        lista.append(char)

  cant = len(lista)
  for i in range(cant-1):
    frecuencia[lista[i]][lista[i+1]] += 1

  P = np.zeros((256, 256), dtype=float)

  for i in range(frecuencia.shape[0]):
    cant = 0
    for j in range(frecuencia.shape[1]):
      cant += frecuencia[i][j]
    for j in range(frecuencia.shape[1]):
      P[i][j] = frecuencia[i][j]/cant


  n = P.shape[0]
  A = np.transpose(P - np.eye(256))
  A = np.vstack([A, np.ones(256)])
  b = np.zeros(257)
  b[-1] = 1
  pi = np.linalg.lstsq(A, b, rcond=None)[0]


  cant = 256
  for i in range(cant):
    for j in range(cant):
      if P[i][j] != 0:
        entropia += pi[i]*P[i][j]*math.log2(1/P[i][j])

  return str(entropia)

print("Entropia el_quijote.txt: " + CalcEntropia('el_quijote.txt'))
print("Entropia el_quijote.7z: " + CalcEntropia('el_quijote.7z'))
print("Entropia txt:" + CalcEntropia('test.txt'))
print("Entropia doc:" + CalcEntropia('test.doc'))
print("Entropia exe:" + CalcEntropia('test.exe'))
print("Entropia rar:" + CalcEntropia('test.rar'))