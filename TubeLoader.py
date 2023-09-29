from pytube import YouTube
import os
from tqdm import tqdm

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
W = '\033[0m'

banner = G + '''
USO PARA TODO PUBLICO.... MadeBy:Python     \(*_*)✓
                                              | |
                                              Y Y
'''
logo_from = R + '''
__   _____  _   _ _____ _   _ ____  _____
\ \ / / _ \| | | |_   _| | | | __ )| ____|
 \ V / | | | | | | | | | | | |  _ \|  _|
  | || |_| | |_| | | | | |_| | |_) | |___
  |_| \___/ \___/  |_|  \___/|____/|_____|
'''
print(banner)
print(logo_from)
url = input("Link Del Video :")

yt = YouTube(url)

# Listar las resoluciones disponibles
resolutions = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

print(Y + "Resoluciones disponibles para video MP4:")
for i, resolution in enumerate(resolutions):
    print(f"{i + 1}. {resolution.resolution}")

# Listar las opciones para descargar como MP3
mp3_stream = yt.streams.filter(only_audio=True).first()
if mp3_stream:
    print(Y + f"{len(resolutions) + 1}. Descargar como MP3")
else:
    print(Y + f"No se encontró una opción para descargar como MP3")

# Solicitar al usuario que elija una opción
choice = int(input("Elija una opción (ingrese el número correspondiente): "))

if 1 <= choice <= len(resolutions):
    # El usuario elige descargar el video en MP4
    yt_stream = resolutions[choice - 1]
    file_extension = "mp4"
elif choice == len(resolutions) + 1 and mp3_stream:
    # El usuario elige descargar el audio en MP3 si está disponible
    yt_stream = mp3_stream
    file_extension = "mp3"
else:
    print("Opción no válida. Saliendo.")
    exit()

# Ruta de descarga en /sdcard/
download_path = "/sdcard/"

# Nombre personalizado para el archivo de descarga
user_input_name = input("Nombre personalizado para el archivo (sin formato): ")

# Agregar el formato de archivo por defecto
file_name = user_input_name + "." + file_extension

# Descarga del video/audio con una barra de progreso
with tqdm(total=yt_stream.filesize, unit='B', unit_scale=True, desc=f'Descargando "{file_name}"') as pbar:
    yt_stream.download(output_path=download_path, filename=file_name)

print(f'\n{G}Descarga completada. El archivo se encuentra en: {download_path}{W}{file_name}')
