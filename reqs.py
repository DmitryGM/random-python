# import requests
# from lxml import html



# name = 'Marilyn Monroe'
# response = requests.get(f'https://www.google.com/search?newwindow=1&biw=1858&bih=1009&tbm=isch&sa=1&ei=gqTzW4NipOyuBKLyioAM&q={name}')
# tree = html.fromstring(response.content)
# lst = tree.xpath("//table[@class='images_table']/tr/td/a/img")
# for img in lst:
#     print('<img src="')
#     print(img.attrib['src'])
#     print('" />')