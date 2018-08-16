# http://www.pythonchallenge.com/pc/def/peak.html
# see the source file
# peak hell sounds like pickle
# download the file banner.p

import pickle

with open("banner.p", "rb") as file:
    content = pickle.load(file)
    print(content)

# here we get a list in content
# I think it may be a image
# then I try to draw it

for line in content:
    for i in range(len(line)):
        for j in range(line[i][1]):
            print(line[i][0], end='')
    print('')
