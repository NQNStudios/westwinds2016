#! /usr/bin/python
import sys
import bs4

lines = []
for x in sys.stdin:
	lines.append(x)
html = "\n".join(lines)

soup = bs4.BeautifulSoup(html)
soup.head.extract()

withheld = False
for x in soup.html.descendants:
	if withheld:
		print(x.encode("utf-8"))
	else:
		withheld = True