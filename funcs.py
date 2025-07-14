#for youtube search
from googleapiclient.discovery import build
import json

API_KEY = "AIzaSyBRfqVb1ezjDGQNYFFgqpjM-X6lz4mbf7I"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
#for youtube search






def split_words_by_minussign():
	s = "this is hello world  -bad code"
	print(s)
	parts = s.split('-', 1)  # split into 2 parts at first '-'

	if len(parts) == 2:
    	print(parts[0].strip())  # print before '-', trimmed
    	print(parts[1].strip())  # print after '-', trimmed
	else:
    	print(s)  # no '-' found, print whole string
def youtube_search(query, max_results=5):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=max_results,
        type="video"
    ).execute()

    results = []
    for idx, item in enumerate(search_response.get('items', []), start=1):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url = f"https://www.youtube.com/watch?v={video_id}"
        results.append({
            "id": idx,
            "name": title,
            "url": url
        })

    return results
    #print(json.dumps(data, indent=4))
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