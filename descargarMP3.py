import yt_dlp
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv() 

# Enlace de YouTube
url = input("Introduce la url del audio, canción o playlist que deseas descargar: \n")

# Carpeta de descarga
output_dir = "downloadsMP3"
os.makedirs(output_dir, exist_ok=True)

# Configuración de yt-dlp para descargar solo audio en formato webm
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': os.getenv('FFMPEG_PATH'),  # Asegúrate de que ffmpeg esté en tu PATH
}

# Descargar audio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    title = info.get('title', None)
    webm_path = os.path.join(output_dir, f"{title}.webm")

# Convertir a MP3
mp3_path = os.path.join(output_dir, f"{title}.mp3")

print(f"✅ Audio convertido a MP3, encuentralo aqui -> : {mp3_path}")