#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += "%c" % (ord(c) - 32)
        else:
            result += "%c" % ord(c)
    print("{}".format(result))