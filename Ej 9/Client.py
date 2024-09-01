import socket

#Socket al que se conecta el cliente
host = '127.0.0.1'
port = 5555

def compress(text):
    #Tabla instantanea para el alfabeto
    dic = {
    'A':'10',
    'B':'110',
    'C':'1110',
    'D':'11110',
    'E':'111110',
    'F':'1111110',
    'G':'11111110',
    'H':'11111111',
    }

    #Convierto cadena segun los codigos de la tabla
    codigo = ""
    for i in range(len(text)):
        codigo += dic[text[i]]
    
   
    #Cuento la cantidad de bit a leer y lo paso a binario
    cant_bits = len(codigo)
    cant_bits = bin(cant_bits)[2:]
   
    #relleno la cantidad de bits para que sea un byte entero
    if len(cant_bits) < 8:
        cant_bits = cant_bits.rjust(8,"0")

    
    #Agrego el byte de cantidad a leer como cabecera
    codigo = cant_bits + codigo
   
    

    #Relleno el ultimo byte del codigo en caso de no ser multiplo de 8
    resto = len(codigo) % 8
    codigo = codigo.ljust(len(codigo)+8-resto,"0")
    
    
    return codigo

#Creo el socket del cliente
#socket.AF_INET = usar IPv4
#socket.SOCK_STREAM = usar TCP
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #Conecto con el servidor
    s.connect((host,port))

    while True:

        send = input("Texto a enviar: ")
        if not send:
            break
        #codifico el codigo
        codigo = compress(send)
        print(f"bytes sin comprimir: {len(send)*8}")
        print(f"bytes sin comprimir: {len(codigo)//8}")
        
        #Envio el codigo como bytes
        byte_data = int(codigo, 2).to_bytes(len(codigo) // 8, byteorder='big')
        s.sendall(byte_data)
