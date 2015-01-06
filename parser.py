#!/usr/bin/python
from bs4 import BeautifulSoup
import codecs
soup = BeautifulSoup(open("subscriptions.xml"))
tags = soup.find_all("outline")
f = codecs.open("links.md","w","utf-8")
for tag in tags:
    # print tag['htmlurl']
    if tag.get('htmlurl') is None:
        f.write("\n##" + tag.get('title')+ "\n\n")
        # print "##" + tag.get('title')
    else:
        f.write("- ["+tag.get('text')+"]("+tag.get('htmlurl')+")  \n")
        # print "- ["+tag.get('text')+"]("+tag.get('htmlurl')+")  "
f.close()
