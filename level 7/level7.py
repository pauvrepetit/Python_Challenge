# level 7
# http://www.pythonchallenge.com/pc/def/oxygen.html
# get the gray part of the image
# change the color model to RGB and convert the number to char using ASCII
# zip the string

from PIL import Image

image = Image.open("oxygen.png")
pix = image.load()
width, height = image.size
print(width, height)
h = 0
w = 0
for h in range(height):
    if pix[0, h] == (0x73, 0x73, 0x73, 255):
        break

for w in range(width):
    if pix[w, h] == (0x41, 0x2F, 0x01, 255):
        break

RGBA = []
for w1 in range(w):
    RGBA.append(pix[w1, h])
print(RGBA)
RGB_char = []
for i in range(len(RGBA)):
    for j in range(3):
        RGB_char.append(chr(RGBA[i][j]))
print(RGB_char)

char_b = RGB_char[0]
RGB_char1 = [char_b]
for i in range(1, len(RGB_char)):
    if RGB_char[i] != char_b:
        RGB_char1.append(RGB_char[i])
        char_b = RGB_char[i]
print(''.join(RGB_char1))

next_char = []
next = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in range(len(next)):
    next_char.append(chr(next[i]))
print(''.join(next_char))