import socket

host = '127.0.0.1'
port = 5555

dic = {
    '10':'A',
    '110':'B',
    '1110':'C',
    '11110':'D',
    '111110':'E',
    '1111110':'F',
    '11111110':'G',
    '11111111':'H',
    
    }
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    print("esperando conexion...")
    newport,adress = s.accept()

    with newport:
        print(f"Conexión por {adress}")
        while True:
            data = newport.recv(1024)
            if not data:
                break
            #leo bytes y los paso a int, aca se pierden los 0 del principio
            integer = int.from_bytes(data,byteorder="big")
            #lo paso a str y borro 0b
            recovered_binary_string = bin(integer)[2:]
            #calculo cantidad de 0 perdidos al principio del codigo
            leading_zeroes = 8-len(recovered_binary_string)% 8
            #añado los primeros 0 faltantes
            recovered_binary_string = recovered_binary_string.zfill(len(recovered_binary_string)+leading_zeroes)
            
            #leo la cantidad de bits a leer del mensaje
            cant_bits = int(recovered_binary_string[:8],2)

            #decofico el mensaje
            text = ""
            letter = ""
            for i in range(8,cant_bits+8):
                letter += recovered_binary_string[i]
                if letter in dic:
                    text += dic[letter]
                    letter = ""
            print(text)
                
            