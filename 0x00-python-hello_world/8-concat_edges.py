#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
auxstr = str[39:67]
auxstr += str[7:10]
auxstr += str[107:112]
auxstr += str[0:6]
str = auxstr
print(str)
