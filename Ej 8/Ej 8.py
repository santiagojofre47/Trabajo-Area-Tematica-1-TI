#Ejercicio 8
#El siguiente algoritmo validador de CUIT se basa en la utilización del algoritmo de Módulo 11 para calcular el digito verificador, el cual es el último digito que figura en un CUIT.

# Definir la función de validación de CUIT
def validar_cuit(cuit):

    digitos_validos = [20, 23, 24, 27, 30, 33, 34]
    primeros_dos_digitos = int(cuit[:2])#obtenemos los primeros dos dígitos del CUIT


    # Validaciones mínimas: evaluamos que la cadena de entrada tenga los 13 caracteres que componen un CUIT, y verificando que contengan los separadores "-", también verificaremos que los primeros dos digitos son los validados
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-" or primeros_dos_digitos not in digitos_validos:
        return False#Si no se cumple, retorna False

    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]#Numeros de la serie numérica que se aplicará como producto con los 10 primeros digitos del CUIT

    cuit = cuit.replace("-", "") # Remuevo las barras

    # Cálculo del dígito verificador
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]#Se aplica el producto del dígito del cuit actual por el número de la serie actual, dicho resultado se acumula en aux


    aux = 11 - (aux - (int(aux / 11) * 11))#Se calcula el digito verificador aplicando el Módulo 11

    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    return aux == int(cuit[10])#Verifica si el resultado obtenido es igual al último dígito del CUIT: True si lo es, false si no lo es

#Ejemplo
cuits = ['20-44127975-3','20-44127975-4','66-44127975-3']

for i in range(len(cuits)):
    if validar_cuit(cuits[i]):
        print(f"{cuits[i]} es un CUIT válido.")
    else:
        print(f"{cuits[i]} no es un CUIT válido.")