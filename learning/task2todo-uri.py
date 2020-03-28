#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import argparse
from urllib.parse import quote

XCALLBACK_URI_TEMPLATE = """twodo://x-callback-url/add?task={}&type=0&forlist={}&tags={}&action=url:{}&edit={}"""


def generate_url(action_url, name="Check url", tags=["url"], project="Research", edit=False):
    param_actionurl = quote(action_url)
    param_name = quote(name)
    param_tags = ",".join([quote(x) for x in tags])
    param_project = quote(project)
    param_edit = int(edit)

    text = XCALLBACK_URI_TEMPLATE.format(param_name, param_project, param_tags, param_actionurl, param_edit)
    return text

def main():
    parser = argparse.ArgumentParser(description="Create task in form of xcallback-uri for 2do app")
    parser.add_argument("url", help="URL to research")
    parser.add_argument("-n", "--name", help="Task name", type=str, default="Check URL")
    parser.add_argument("-p", "--list", help="List to save", type=str, default="Research")
    parser.add_argument("-q", "--quiet", help="Don't show 2do popup for task creation", default=True, action="store_false")
    parser.add_argument("-t", "--tags", help="Tags", nargs="+", default=["url"])
    
    args = parser.parse_args()
    print(generate_url(args.url, args.name, args.tags, args.list, args.quiet))

if __name__ == "__main__":
    main()