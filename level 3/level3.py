# http://www.pythonchallenge.com/pc/def/ocr.html
# download the source file and save the comment to ocr.txt
# there is a comment saying "find rare characters in the mess below:"

import re

with open("ocr.txt") as file:
    lines = file.read()

count = {}

for char in lines:
    try:
        count[char] += 1
    except KeyError:
        count.update({char: 1})

print(count)

for key, value in count.items():
    if value == 1:
        print(key, end='')

print('')

# goto http://www.pythonchallenge.com/pc/def/equality.html
# download the source file and save the comment to equality.txt
# the website said that "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."

re_string = re.compile(r"[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")
with open("equality.txt") as file2:
    lines = file2.read()

line = []
for char in lines:
    if char != '\n':
        line.append(char)

line = ''.join(line)
match = re_string.findall(line)
print(match)

for i in range(len(match)):
    print(match[i][4], end='')
