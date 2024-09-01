#Ejercicio 5

#Python utiliza un byte por caracter, elijo 20 como cantidad fija de bytes
cantBytes = 20
#Byte de 8 unos que se utiliza con las mascaras para guardar la información de las preguntas bivaluadas
byte_bivaluado = 255 

band = True
while band:
    NyA = bytes(input("Nombre y Apellido: "),"utf-8")
    Dirección = bytes(input("Direccion: "),"utf-8")
    Dni = bytes(input("Dni: "),"utf-8")

    if len(NyA) <= cantBytes and len(Dirección) <= cantBytes or len(Dni) <= cantBytes:
        band = False
    else:
        print(f"Catidad de caracteres debe ser menor a {cantBytes}")


#Guardo los datos no bivaluados en un diccionario para mas facil maenejo
datos_string = {
    "NyA": NyA,
    "Direccion" : Dirección,
    "Dni" : Dni,
}

#Para cada pregunta si la respuesta es no utilizo una mascara para colocar el bit correspondiente en 0. Ej 11111111 and 01111111

if input("Estudios primarios: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 127 
   
if input("Estudios secundarios: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 191

if input("Estudios universitarios: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 223

if input("Vivienda propia: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 239

if input("Soltero: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 247

if input("Hijos: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 251

if input("Empleado: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 253

if input("Algo: y/n ").lower() == "n":
    byte_bivaluado = byte_bivaluado & 254


#Para las entradas menores a 20 caracteres las relleno con el simbolo -
for key,value in datos_string.items():
   if len(value) < cantBytes:
    datos_string[key] = datos_string[key].ljust(cantBytes,b'-')

#Escribo los datos en el archivos, siempre va a ser de 61 B de tamaño
with open("fijos.dat", 'w+b') as f:
    f.write(datos_string["NyA"])
    f.write(datos_string["Direccion"])
    f.write(datos_string["Dni"])
    f.write(byte_bivaluado.to_bytes(1,"little"))
    
 
   

        