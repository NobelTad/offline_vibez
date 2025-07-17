import yt_dlp
import requests
import re
import os
import eyed3
from eyed3.id3.frames import ImageFrame
from PIL import Image

def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_as_mp3_with_thumbnail(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = clean_filename(info.get("title", "audio"))
        thumbnail_url = info.get("thumbnail")
        mp3_filename = f"{title}.mp3"

    print(f"[+] Downloaded MP3: {mp3_filename}")
    print(f"[+] Downloading and resizing thumbnail...")

    headers = {'User-Agent': 'Mozilla/5.0'}
    thumb_data = requests.get(thumbnail_url, headers=headers).content
    raw_thumb_path = "temp_thumb.jpg"
    resized_thumb_path = "resized_thumb.jpg"

    # Save original
    with open(raw_thumb_path, "wb") as f:
        f.write(thumb_data)

    # Convert and resize for player compatibility
    img = Image.open(raw_thumb_path).convert("RGB")
    img = img.resize((300, 300))
    img.save(resized_thumb_path, format="JPEG")
    mime_type = "image/jpeg"

    print(f"[+] Embedding resized thumbnail into MP3...")

    audiofile = eyed3.load(mp3_filename)
    if audiofile.tag is None:
        audiofile.initTag()
        audiofile.tag.save()

    with open(resized_thumb_path, "rb") as img_f:
        image_data = img_f.read()

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, image_data, mime_type)
    audiofile.tag.title = title
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    print(f"[✓] Done. Saved as '{mp3_filename}' with cover art.")

    # Verify embedded image
    print("[i] Verifying embedded image...")
    audiofile = eyed3.load(mp3_filename)
    if audiofile.tag and audiofile.tag.images:
        for img in audiofile.tag.images:
            print(f"  -> Embedded image: {len(img.image_data)} bytes, type={img.mime_type}")
    else:
        print("  [x] No embedded image found!")

    print(f"[i] Thumbnail kept at: {resized_thumb_path}")

# Example usage
if __name__ == "__main__":
    download_as_mp3_with_thumbnail("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
