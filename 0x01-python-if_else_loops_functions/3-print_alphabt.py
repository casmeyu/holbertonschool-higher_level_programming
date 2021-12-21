#!/usr/bin/python3
char = ord('a') #ascii
alphabet = ""
while (char <= ord('z')):
    if (char != ord('q') and char != ord('e')):
        alphabet += chr(char)
    char += 1 
print(alphabet, end = '')
