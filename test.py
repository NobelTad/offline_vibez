import requests
import re

def download_youtube_poster(video_url, filename="poster.jpg"):
    # Extract video ID from URL
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", video_url)
    if not match:
        print("[-] Invalid YouTube URL")
        return

    video_id = match.group(1)
    print(f"[+] Found video ID: {video_id}")

    # Try to get high resolution thumbnail
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    fallback_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    response = requests.get(thumbnail_url)
    if response.status_code != 200:
        print("[!] High-res not found, using fallback.")
        response = requests.get(fallback_url)

    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"[✅] Poster downloaded as '{filename}'")

# 🔁 Example usage:
download_youtube_poster("https://www.youtube.com/watch?v=1XzY2ij_vL4")
