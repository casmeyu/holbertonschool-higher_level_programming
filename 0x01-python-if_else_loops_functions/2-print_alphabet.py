#!/usr/bin/python3
char = ord('a') #ascii
alphabet = ""
while (char <= ord('z')):
    alphabet += chr(char)
    char += 1 
print(alphabet, end = '')
