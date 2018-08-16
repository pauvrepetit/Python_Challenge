# http://www.pythonchallenge.com/pc/def/274877906944.html
# http://www.pythonchallenge.com/pc/def/map.html

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr" \
          " ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

realMessage = []

for char in message:
    if ord('a') <= ord(char) <= ord('x'):
        realMessage.append(chr(ord(char) + 2))
    elif char == 'y':
        realMessage.append('a')
    elif char == 'z':
        realMessage.append('b')
    else:
        realMessage.append(char)
print(''.join(realMessage))

message = "map"
realMessage = []

for char in message:
    if ord('a') <= ord(char) <= ord('x'):
        realMessage.append(chr(ord(char) + 2))
    elif char == 'y':
        realMessage.append('a')
    elif char == 'z':
        realMessage.append('b')
    else:
        realMessage.append(char)
print(''.join(realMessage))
