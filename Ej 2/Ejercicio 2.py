import struct

# Establecemos formato de los bloques de la cabecera.< especifica leer todo como little endian, 2s string de 2 bytes, I entero sin signo de 4 bytes, H entero sin signo de 2 bytes
bmp_header_format = (
    '<2s'   # Signature
    'I'    # FileSize
    'I'    # Reserved
    'I'    # DataOffset
    'I'    # Size
    'I'    # Width
    'I'    # Height
    'H'    # Planes
    'H'    # Bitcount
    'I'    # Compression
    'I'    # ImageSize
    'I'    # XPixelsPerM
    'I'    # YPixelsPerM
    'I'    # ColorsUsed
    'I'    # ColorsImportant
)


with open('Ej 2\example_small.bmp', 'rb') as f: # Leemos el archivo como bytes
    # Leemos primeros 44 bytes
    header_data = f.read(54)
    # Leemos los datos segun la estructura establecida
    unpacked_data = struct.unpack(bmp_header_format, header_data)
    
    # Los guardamos en un diccionario
    header = {
        'Signature': unpacked_data[0].decode('utf-8'),
        'FileSize': unpacked_data[1],
        'Reserved': unpacked_data[2],
        'DataOffset': unpacked_data[3],
        'Size': unpacked_data[4],
        'Width': unpacked_data[5],
        'Height': unpacked_data[6],
        'Planes': unpacked_data[7],
        'Bitcount': unpacked_data[8],
        'Compression': unpacked_data[9],
        'ImageSize': unpacked_data[10],
        'XPixelsPerM': unpacked_data[11],
        'YPixelsPerM': unpacked_data[12],
        'ColorsUsed':unpacked_data[13],
        'ColorsImportant':unpacked_data[14]
    }


if header['Signature'] == 'BM':
    for key, value in header.items():
        print(f"{key}: {value}")
else:
    print("no es .bmp")

