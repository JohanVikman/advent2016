from __future__ import print_function
import hashlib
import re

def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    string_position_frequencies = [dict(),
                                   dict(),
                                   dict(),
                                   dict(),
                                   dict(),
                                   dict(),
                                   dict(),
                                   dict()]
    for line in lines.split("\n"):
        if len(line) == 0:
            continue
        for i in range(0,8):
            char = line[i]
            if string_position_frequencies[i].has_key(char):
                string_position_frequencies[i][char] = string_position_frequencies[i][char] + 1
            else:
                string_position_frequencies[i][char] = 1

    for d in string_position_frequencies:
        min=99999999999999
        min_char = ""
        for char in d.iterkeys():
            if d[char] < min:
                min=d[char]
                min_char=char
        print("{}".format(min_char),end="")
    

if __name__ == '__main__':
    run()
