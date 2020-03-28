import argparse
import datetime

DESCRIPTION = "Convert markdown to hugo post page"

HUGO_POST_FORMAT = """---
title: "{}"
date: {}
---

<!--more-->

"""

def convert(source, dest, img_dest, time):
    assert isinstance(source, file)
    assert isinstance(dest, file)

    # create heading
    title = source.readline().split("# ")[1].replace('\n', '')

    if time is None:
        time_now = datetime.datetime.now()
        time = "{}-{}-{}".format(time_now.year, time_now.month, time_now.day)

    head = HUGO_POST_FORMAT.format(title, time)
    dest.write(head)

    data = ""
    for l in source.readlines():
        line = l.replace("img/", "/img/" + img_dest)
        data += line
    
    dest.write(data)
    

def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    
    # arguments list
    parser.add_argument(dest='src', 
                        metavar="src_file", 
                        type=argparse.FileType("r"),
                        help="Markdown file")
    parser.add_argument(dest='dst', 
                        metavar="dst_file", 
                        type=argparse.FileType("w"),
                        help="Hugo-converted file")

    parser.add_argument('-d', dest='date', metavar='DATE', type=str,
                        help="Post creation date in format YYYY-MM-DD", default=None)

    parser.add_argument('-i', dest='img', metavar='SUBDIR', type=str,
                        help="Subdirectory of '/img'", default="")

    args = parser.parse_args()
    convert(args.src, args.dst, '{}/'.format(args.img), args.date)


if __name__ == "__main__":
    main()
