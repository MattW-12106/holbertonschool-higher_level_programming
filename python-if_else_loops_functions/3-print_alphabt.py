#!/usr/bin/python3
for i in range(97, 123): #iterate through ASCII values of a-z
    if i != 101 and i != 113: #skip 'e' (101) and 'q' (113)
        print("%c" % i, end="") #print character without newline