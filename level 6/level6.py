# http://www.pythonchallenge.com/pc/def/channel.html
# I find a zip in the comment of the source code
# try http://www.pythonchallenge.com/pc/def/channel.zip and get a zipfile

# use 7-zip to unzip the file and get detail output, save it in channel.txt
# see the readme.txt to know that we need to begin at 90052

import re


re_num = re.compile(r"\d+")
path = "channel/90052.txt"
content = []

while True:
    try:
        file = open(path)
        content = file.read()
        old_num = re_num.findall(path)[0]
        new_num = re_num.findall(content)[0]
        path = path.replace(old_num, new_num)
        file.close()
    except IndexError:
        break
    except FileNotFoundError:
        break
print(content)
print(path)

# get the next hint "Collect the comments."
# then we need to gather the comments in the zip file
# we can see that every file unzipped from channel.zip has a comment
# and we can get them from channel.txt

channel = open("channel.txt")
content_channel = channel.read()
path = "channel/90052.txt"
comment = []

while True:
    try:
        file = open(path)
        content = file.read()
        old_num = re_num.findall(path)[0]
        new_num = re_num.findall(content)[0]
        comment.append(content_channel[
                           content_channel.find("Comment", content_channel.find(old_num + ".txt")) + 10])
        path = path.replace(old_num, new_num)
        file.close()
    except IndexError:
        break
    except FileNotFoundError:
        break
print(''.join(comment))

# now we get a long string
# copy it to an editor and I find that maybe I need to change '_' to '\n'

comment2 = []
for char in comment:
    if char == '_':
        char = '\n'
    comment2.append(char)
print(''.join(comment2))

# change the url to hockey.html
# we get a message "it's in the air. look at the letters. "
# then we change the url to oxygen.html
