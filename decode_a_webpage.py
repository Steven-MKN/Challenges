import requests

r = requests.get('https://www.nytimes.com')

string = str(r)
print(string)
title = string.find('<h2 class="css-6h3ud0 esl82me2">', 0, 30)
print(title)
