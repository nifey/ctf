string = 'wAPcULZh\x7f\x06x\x04LDd\x06~Z"YtJ'

i = 0
for char in string:
    if (i % 2 == 0):
        print (chr(ord(char) ^ 0x13), end="")
    else:
        print (chr(ord(char) ^ 0x37), end="")
    i = i + 1
