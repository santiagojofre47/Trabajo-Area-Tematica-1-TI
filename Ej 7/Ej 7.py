#Ejercicio 7

#Implementación 1:  Distancia de Jaccard
#Esta implementación se basa en la teoría de conjuntos. Dado dos cadenas, se calcula la unión de ambas y su intersección.
#Posteriormente, se divide la cantidad de caracteres coincidentes de la intersección con la cantidad de caracterés de la unión del conjunto resultante. El resultado obtenido, indica la similitud de esas cadenas

# Definir la función de similitud de Jaccard
def jaccard_similarity(s1, s2):
    set1 = set(s1)#Se genera un conjunto de carácteres a partir de la cadena "s1". Nota: el conjunto resultante no tendrá carácteres repetidos
    set2 = set(s2)#Idem para la cadena "s2"

    intersection = len(set1.intersection(set2))#Calculamos intersección: el resultado indicará el numero de carácteres coincidentes en s1 y s2
    union = len(set1.union(set2))#Se realiza la union del conjunto s1 y s2 y se cuenta la cantidad de elementos
    return round((intersection / union)*100,2)#Realiza el cociente, y obtiene el resultado en porcentajes

#Implmentación 2: Distancia de Hamming
#Esta implementación se basa en obtener el numero de posiciones en las que dos cadenas difieren. Nota: las cadenas deben ser de igual longuitud, por lo que solo es aplicable para ese caso.

# Definir la función de distancia de Hamming
def distancia_hamming(s1, s2):
    if len(s1) != len(s2):#Primero, evaluamos que ambas cadenas tengan igual longuitud
        raise ValueError("Las cadenas deben tener la misma longitud!")
    cant_dif =  sum(c1 != c2 for c1, c2 in zip(s1, s2))#Para obtener la Distancia de Hamming, se define una lista por comprensión mediante el método zip, que permitira emparejar los carácteres de ambas cadeas y poder asi comparar cada par. Se cuenta cuántas veces los caracteres son diferentes (caracter1 != caracter2).
    porcentaje_similitud = 100 - (cant_dif/len(s1))*100#Obtenemos el porcentaje de similitud entre ambas cadenas
    return round(porcentaje_similitud,2)

# Ejemplo
cadenas = ["Horacio Perez", "Oracio Perez", "Manuel Belgrano", "Manuel Delgrano"]
s1 = cadenas[0]
s2 = cadenas[1]
s3 = cadenas[2]
s4 = cadenas[3]

distancia = distancia_hamming(s3, s4)
print(f"Distancia de Hamming. Similitud entre '{s3}' y '{s4}': {distancia}%")

similarity = jaccard_similarity(s1, s2)
print(f"Similitud de Jaccard entre '{s1}' y '{s2}': {similarity}%")