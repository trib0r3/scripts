import pyperclip
import re
import sys

# get raw code
raw = pyperclip.paste()

# create pattern & get shellcode lines
pattern = re.compile(r'"[\\|x|\d|a-f|A-F]*"')
matches = pattern.findall(raw)

if len(matches) is 0:
    print 'Error: Invalid arg!'
    sys.exit(1)


# format
res = ""
for line in matches:
    res += line

res = res.replace("\"", "")


# copy result to clipboard
pyperclip.copy('"' + res + '"')

