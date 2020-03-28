import requests
from sys import argv
import re
import html

SEPARATOR = ", a song by "
END = " on Spotify"

def main():
    if len(argv) < 2:
        print("{} <spotify url1> <sporify url2> ...".format(argv[0]))
        return

    for url in argv[1:]:
        html_text = requests.get(url).text
        m = re.search(r'<title>(.*)</title>', html_text)

        if m is None:
            print("{} Something went wrong, can't find song title".format(url))
            continue
        
        text = html.unescape(m.group(1))
        sep_pos = text.find(SEPARATOR)
        title = text[:sep_pos]
        author = text[sep_pos + len(SEPARATOR):text.find(END)]

        print("{} - {}".format(author, title))

if __name__ == "__main__":
    main()
