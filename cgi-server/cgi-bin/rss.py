#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Content-type: text/html\n")


import html as html_
import requests
import xml.etree.ElementTree as ElementTree
from pymongo import MongoClient
import cgi
# from lxml import html
# import random
# from lxml import etree
# import pymongo


client = MongoClient('localhost', 27017)
db = client.mydb


# Form:
form = cgi.FieldStorage()
new_rss = form.getfirst("new_rss", "null")
if (new_rss != "null"):
    db.rss.insert_one({'src': new_rss})

# Update DB:
# https://habr.com/rss/interesting/
# https://news.yandex.ru/world.rss

for rss in db.rss.find():
    try:
        print(rss['src'])
        response = requests.get(rss['src'])
        root = ElementTree.fromstring(response.content)

        for src, title in zip(root.iter('guid'), list(root.iter('title'))[2:]):
            doc = {'title': title.text, 'src': src.text}

            if not list(db.test.find(doc)):
                # print('NEW!')
                db.test.insert_one(doc)
    except:
        pass

print("""<!DOCTYPE HTML>
<html>
<head>  
<title>RSS</title>
</head>
<body>""")

print("<table>")
for doc in db.test.find():
    try:
        if '\u200a' in doc['title']:
            continue
        print(f"""<tr><td><a href="{doc['src']}">{doc['title']}</a></td></tr>""")
    except KeyError:
        pass
print("</table>")

print(f"""
<h2>Form:</h2>
<form method="post" action="rss.py">
<input type="text" value="" name="new_rss" />
<input value="Добавить ленту" type="submit">
</form>
</body>
</html>
""")
