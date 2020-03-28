# Dump songs based on spotify urls

# urls.txt schema:
#   https://open.spotify.com/track/...
#   https://open.spotify.com/track/...

import requests
import re
import json

def main():
    urls = None
    with open('urls.txt', 'r') as f:
        urls = f.readlines()
        f.close()

    if urls is None:
        print("Can't find 'urls.txt' file in local directory")
        return

    for u in urls:
        r = requests.get(u)
        m = re.search(r'Spotify.Entity = (.*)', r.text)
        d = json.loads(m.group(1)[:-1])

        name = d['name']
        artists = ','.join(e['name'] for e in d['artists'])

        print('{} - {}'.format(artists, name))

if __name__ == "__main__":
    main()
