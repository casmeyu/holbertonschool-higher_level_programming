#!/usr/bin/python3
"""Text indentation based on many delimiters"""


def text_indentation(text):
    """text indentation based on delimiters
        Args:
            text(str): text to indent
            based on delimiter and indentation
    """
    delimiters = ".?:"
    lines = []
    line = ""
    l_len = 0

    if (type(text) is not str):
        raise TypeError("text must be a string")

    for char in text:
        if (char in delimiters):
            line += char
            line = line.strip()
            lines.append(line)
            line = ""
        else:
            line += char

    if (len(line) > 0):
        line = line.strip()
        lines.append(line)
        line = ""

    l_len = len(lines)
    for idx in range(l_len):
        if (idx == (len(lines) - 1)):
            print(lines[idx], end='')
        else:
            print("{}\n".format(lines[idx]))
