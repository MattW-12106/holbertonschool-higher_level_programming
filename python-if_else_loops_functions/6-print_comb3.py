#!/usr/bin/python3
for i in range(10): # outer loop for the first digit
    for j in range(i + 1, 10): # inner loop for the second digit
        print("{:d}{:d}".format(i, j), end=", " if i != 8 else "\n") # print the combination with formatting