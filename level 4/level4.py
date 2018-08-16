# http://www.pythonchallenge.com/pc/def/linkedlist.php

# part one
# in the website there is a href "linkedlist.php?nothing=12345"
# click it and then we go to "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
# follow it

# part two
# we get the url "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044"
# and a hint "Yes. Divide by two and keep going."
# then change the beginning url to "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"

# part three
# we get the url "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82683"
# and a hint "You've been misleaded to here. Go to previous one and check."
# then we output every number while running the program.
# and we find the previous number 82682
# go the this page and get the true number 63579
# change the beginning url to "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"

from urllib import request, error
import re

re_num = re.compile(r"\d+")
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"


while True:
    try:
        content = request.urlopen(url).read().decode('utf-8')
        old_num = re_num.findall(url)[0]
        new_num = re_num.findall(content)[0]
        print(old_num)
        url = url.replace(old_num, new_num)
    except error.HTTPError:
        break
    except IndexError:
        break
print(url)
print(content)
