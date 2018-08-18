# http://www.pythonchallenge.com/pc/def/integrity.html
# see the source code and find the un and pw
# two strings begin as "BZ"
# using bz2 to decompress the strings and get the username and password

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))
