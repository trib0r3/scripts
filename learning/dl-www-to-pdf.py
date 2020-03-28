#
# Download WWW pages & convert it into PDF pages
#
# File required: 'style.css' (or delete it from code)
# Files are saved under path <DirectoryName>/interesting-article
# (for url: http://somewebsite.com/somecategory/some/interesting-article)
#

__author__ = "sheadovas"

import pdfkit
import requests
from bs4 import BeautifulSoup

def get_post_html(url):
    page = requests.get(url)
    if page.status_code is not 200:
        print "Error, cannot open: '{}'".format(url)
        return

    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find_all('main', id='main', class_='site-main')[0]
    return body
    

def parse_to_pdf(content, dstfile):
    TEMPLATE = u"""
    <html>
        <head>
            <meta name="pdfkit-page-size" content="Legal"/>
            <meta name="pdfkit-orientation" content="Landscape"/>
            <meta charset="UTF-8">
        </head>
        <body>
        {}
        </body>
    </html>"""

    html = TEMPLATE.format(content)
    
    try:
        pdfkit.from_string(html, dstfile, css='./style.css')
    except Exception as e:
        print "!!! Error, Ignore: {}".format(e.strerror)

urls = [
  # TODO enter urls HERE, example:
  ["DirectoryName","http://somewebsite.com/interesting-artice"]
]

i = 1
for pair in urls:
    print "==> [{}/{}]".format(i, len(urls))
    i += 1

    category, url = pair
    print "==> {} : {}".format(category, url)
    body = get_post_html(url)
    
    title = url.split('/')
    filename = "{}/{}.pdf".format(category, title[len(title)-2])

    parse_to_pdf(body, filename)

