#!/usr/bin/env python3
import cgi
import html as html_
import requests
from lxml import html
import random


form = cgi.FieldStorage()
selected_answer = form.getfirst("selected_answer", "null")
right_answer = form.getfirst("right_answer", "null")
level = form.getfirst("level", "null")



selected_answer = html_.escape(selected_answer)
right_answer = html_.escape(right_answer)
level = html_.escape(level)

max_number = 10
if level == '1-50':
    max_number = 50
if level == '1-100':
    max_number = 100


names = [
'Marilyn Monroe',
'Abraham Lincoln',
'Mother Teresa',
'John F. Kennedy',
'Martin Luther King',
'Nelson Mandela',
'Queen Elizabeth II',
'Winston Churchill',
'Donald Trump',
'Bill Gates',
'Muhammad Ali',
'Mahatma Gandhi',
'Margaret Thatcher',
'Christopher Columbus',
'Charles Darwin',
'Elvis Presley',
'Albert Einstein',
'Paul McCartney',
'Queen Victoria',
'Pope Francis',
'Jawaharlal Nehru',
'Leonardo da Vinci',
'Vincent Van Gogh',
'Franklin D. Roosevelt',
'Pope John Paul II',
'Thomas Edison',
'Rosa Parks',
'Aung San Suu Kyi',
'Lyndon Johnson',
'Ludwig Beethoven',
'Oprah Winfrey',
'Indira Gandhi',
'Eva Peron',
'Benazir Bhutto',
'George Orwell',
'Desmond Tutu',
'Dalai Lama',
'Walt Disney',
'Neil Armstrong',
'Peter Sellers',
'Barack Obama',
'Malcolm X',
'J.K.Rowling',
'Richard Branson',
'Pele',
'Angelina Jolie',
'Jesse Owens',
'Ernest Hemingway',
'John Lennon',
'Henry Ford',
'Haile Selassie',
'Joseph Stalin',
'Lord Baden Powell',
'Michael Jordon',
'George Bush Jnr',
'Vladimir Lenin',
'Ingrid Bergman',
'Fidel Castro',
'Leo Tolstoy',
'Pablo Picasso',
'Oscar Wilde',
'Coco Chanel',
'Charles de Gaulle',
'Amelia Earhart',
'John M Keynes',
'Louis Pasteur',
'Mikhail Gorbachev',
'Plato',
'Adolf Hitler',
'Sting',
'Mary Magdalene',
'Alfred Hitchcock',
'Michael Jackson',
'Madonna',
'Mata Hari',
'Cleopatra',
'Grace Kelly',
'Steve Jobs',
'Ronald Reagan',
'Lionel Messi',
'Babe Ruth',
'Bob Geldof',
'Leon Trotsky',
'Roger Federer',
'Sigmund Freud',
'Woodrow Wilson',
'Mao Zedong',
'Katherine Hepburn',
'Audrey Hepburn',
'David Beckham',
'Tiger Woods',
'Usain Bolt',
'Carl Lewis',
'Prince Charles',
'Jacqueline Kennedy Onassis',
'C.S. Lewis',
'Billie Holiday',
'J.R.R. Tolkien',
'Billie Jean King',
'Anne Frank',
]

name = random.choice(names[:max_number])
response = requests.get(f'https://www.google.com/search?newwindow=1&biw=1858&bih=1009&tbm=isch&sa=1&ei=gqTzW4NipOyuBKLyioAM&q={name}')
tree = html.fromstring(response.content)
lst = tree.xpath("//table[@class='images_table']/tr/td/a/img")




print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Form</title>
        </head>
        <body>""")

print("<h1>Form:</h1>")
print(f"<p>selected_answer: {selected_answer}</p>")
print(f"<p>right_answer: {right_answer}</p>")
print(f"<p>level: {level}</p>")

print(f'<img src="{random.choice(lst).attrib["src"]}" />')

print('<form action="form.py">')

print('<select name="selected_answer">')
for n in names[:max_number]:
    print(f'<option>{n}</option>')
print('</select>')

print(f"""
<br />
Choose level:
<select name="level">
<option {'selected' if level == '1-10' else ''}>1-10</option>
<option {'selected' if level == '1-50' else ''}>1-50</option>
<option {'selected' if level == '1-100' else ''}>1-100</option>
</select>
<br />
<input type="text" value="{name}" hidden=true name="right_answer" />
<input type="submit">
</form>
</body>
</html>
""")
