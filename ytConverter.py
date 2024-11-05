import yt_dlp #Terminal: pip install yt-dlp
import os
from urllib.parse import urlparse

def convert(url, format, quality):
    try:
        if not format:
            if not os.path.exists('audios'): os.makedirs('audios')
            quality = "320" if not quality else "192"  #32,64,96,128,160,192(AVERAGE),256,320(HIGH)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': quality,
                }],
                'outtmpl': f'audios/%(title)s.%(ext)s', #folder/fileName.extension
                'quiet': True,
                'no_warnings': True   
            }
            print("Downloading to 'audios/' folder...")
        else:
            if not os.path.exists('videos'): os.makedirs('videos')
            quality = "1080" if not quality else "480" #144,240,360,480(AVERAGE),720,1080(HIGH)
            ydl_opts = {
                'format': f'bestvideo[height<={quality}]+bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4'
                }],
                'outtmpl': f'videos/%(title)s.%(ext)s',
                'quiet': True,
                'no_warnings': True   
            }
            print("Downloading to 'videos/' folder...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download successful!")

    except Exception as e: print(f"Error: {e}")

print("<< YOUTUBE CONVERTER>>")
# print(f"[i]: yt-dlp V.{yt_dlp.version.__version__}")
while True:
    url = input("YouTube URL: ")
    while not url.strip() or not all([urlparse(url).scheme, urlparse(url).netloc]): url = input("Invalid or empty URL, try again: ")
    print("Format: [ENTER] MP3 Audio [ANY KEY] MP4 video"); format = input("[>]: ")
    print("Quality: [ENTER] High [ANY KEY] Average"); quality = input("[>]: ")
    convert(url,format,quality)
