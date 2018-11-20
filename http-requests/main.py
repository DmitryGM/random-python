import requests
from lxml import html


if __name__ == '__main__':
    pass
    # response = requests.get('https://httpbin.org/get')
    # print(response.json())


# response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
# print(response.json())


response = requests.get('https://www.google.com/search?newwindow=1&biw=1858&bih=1009&tbm=isch&sa=1&ei=gqTzW4NipOyuBKLyioAM&q=random')
print()

# print(response.content)


# print(response.content)
# '<html><head></head><body> <div id=1></div> <div id=2></div> </body></html>'
tree = html.fromstring(response.content)
# lst = tree.xpath("//*[@id='rg_s']/div")
lst = tree.xpath("//table[@class='images_table']/tr/td/a/img")
# print(lst)
# print(len(lst))
for img in lst:
    print(img.attrib['src'])

# https://www.google.com/search?newwindow=1&biw=1858&bih=1009&tbm=isch&sa=1&ei=gqTzW4NipOyuBKLyioAM&q=8888882
