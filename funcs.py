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