#! /usr/bin/python
import sys
import bs4

lines = []
for x in sys.stdin:
	lines.append(x)
html = "\n".join(lines)

soup = bs4.BeautifulSoup(html)
soup.head.clear()
contents="\n".join(soup.html.strings)
print(contents)