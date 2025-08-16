import yt_dlp
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv() 

# Enlace de YouTube
url = input("Introduce la url del video o playlist que deseas descargar: \n")

# Carpeta de descarga
output_dir = "downloadsMP4"
os.makedirs(output_dir, exist_ok=True)

# Configuración de yt-dlp para descargar video en formato MP4
# Se utiliza 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' para asegurar la mejor calidad de video y audio
# y 'FFmpegVideoConvertor' para convertir el video a MP4 si es necesario.
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'ffmpeg_location': os.getenv('FFMPEG_PATH'),  #! Asegúrate de que ffmpeg esté en tu PATH
}

# Descargar video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    title = info.get('title', None)
    webm_path = os.path.join(output_dir, f"{title}.webm")

# Convertir a MP4
mp4_path = os.path.join(output_dir, f"{title}.mp4")

print(f"✅ Video convertido a MP4, encuéntralo aquí -> : {mp4_path}")