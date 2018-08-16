# http://www.pythonchallenge.com/pc/def/ocr.html
# download the source file and save the comment to ocr.txt
# there is a comment saying "find rare characters in the mess below:"

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
