import urllib.request
from bs4 import  BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup  = BeautifulSoup(html_doc,
                      "html.parser")
                      # from_encoding = "utf-8")

links = soup.find_all("a", href=re.compile("ill"))
for link in links:
    print(link.name, link["href"], link.get_text())

# print("获取Lacie url链接")
# link_node = soup.find("p", href=re.compile("ill"))
# print(link_node.name, link_node["href"], link_node.get_text())

