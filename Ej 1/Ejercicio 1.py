import struct

# Establecemos formato de los bloques de la cabecera. 4s string de 4 bytes, I entero sin signo de 4 bytes, H entero sin signo de 2 bytes
wav_header_format = (
    '4s'   # ChunkID
    'I'    # ChunkSize
    '4s'   # Format
    '4s'   # Subchunk1ID
    'I'    # Subchunk1Size
    'H'    # AudioFormat
    'H'    # NumChannels
    'I'    # SampleRate
    'I'    # ByteRate
    'H'    # BlockAlign
    'H'    # BitsPerSample
    '4s'   # Subchunk2ID
    'I'    # Subchunk2Size
)


with open('Ej 1\BMW+DRIVEBY.wav', 'rb') as f: # Leemos el archivo como bytes
    # Leemos primeros 44 bytes
    header_data = f.read(44)
    # Leemos los datos segun la estructura establecida
    unpacked_data = struct.unpack(wav_header_format, header_data)
    
    # Los guardamos en un diccionario
    header = {
        'ChunkID': unpacked_data[0].decode('utf-8'),
        'ChunkSize': unpacked_data[1],
        'Format': unpacked_data[2].decode('utf-8'),
        'Subchunk1ID': unpacked_data[3].decode('ascii'),
        'Subchunk1Size': unpacked_data[4],
        'AudioFormat': unpacked_data[5],
        'NumChannels': unpacked_data[6],
        'SampleRate': unpacked_data[7],
        'ByteRate': unpacked_data[8],
        'BlockAlign': unpacked_data[9],
        'BitsPerSample': unpacked_data[10],
        'Subchunk2ID': unpacked_data[11].decode('utf-8'),
        'Subchunk2Size': unpacked_data[12],
    }





#Comprobamos el .wav
if header['ChunkID'] == 'RIFF' and header['Format'] == 'WAVE' and header['Subchunk1ID'] == 'fmt ':
    for key, value in header.items():
        print(f"{key}: {value}")
else:
    print("No es un archivo .wav")