import requests
import base64

CLIENT_ID = 'f4a338329b344b65b6c39f63392bc33f'
CLIENT_SECRET = 'dd4095583c7744528d99e7f9f2ea7556'

def get_token():
    creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    token = base64.b64encode(creds.encode()).decode()
    resp = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={'Authorization': f'Basic {token}'},
        data={'grant_type': 'client_credentials'}
    )
    return resp.json()['access_token']

def search_song(query):
    token = get_token()
    resp = requests.get(
        'https://api.spotify.com/v1/search',
        headers={'Authorization': f'Bearer {token}'},
        params={'q': query, 'type': 'track', 'limit': 1}
    )
    data = resp.json()
    item = data['tracks']['items'][0]
    artist = item['artists'][0]['name']
    track = item['name']
    return artist, track

if __name__ == '__main__':
    q = input("Enter song to search: ")
    artist, track = search_song(q)
    print(f"🎵 Artist: {artist}\n🎶 Track: {track}")
