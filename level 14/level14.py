# level 14
# http://www.pythonchallenge.com/pc/return/italy.html
# username: huge
# password: file

from PIL import Image, ImageDraw

image = Image.open('wire.png')
pix = image.load()
width = image.size[0]
height = image.size[1]
print(width, height)

image2 = Image.new("RGB", (4 * 99, 50), '#ffffff')
draw = ImageDraw.Draw(image2)
w = 0
for y in range(50):
    for x in range(4 * (99 - 2 * y)):
        draw.point((x, y), fill=pix[w, 0])
        w = w + 1
image2.show()
