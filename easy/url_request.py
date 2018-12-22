import urllib.request
import  http.cookiejar
# urllib2 ==  urllib.request

web_url = "http://www.baidu.com"
# response = urllib.request.urlopen(web_url)
# content = response.read()
# print(content)
#
# request = urllib.request.Request(urllib)
# request.data = ("a","1")
# request.add_header("User-Agent", "Mozilla/5.0")

# request = urllib.request.urlopen(web_url)
# print(request.getcode())
# print(request.read())

# request = urllib.request.Request(web_url)
# request.add_header("User-Agent", "Mozilla/5.0")
# # request.data = ("a", 1)
# response = urllib.request.urlopen(request)
# print(response.getcode())
# print(response.read())

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response = urllib.request.urlopen(web_url)
print(response.getcode())
print(response.read())
