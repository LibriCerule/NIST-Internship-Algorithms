#!/usr/bin/python2
import sys

with open(sys.argv[1], "r") as FILE:
    with open('out.txt', 'w') as w:
        for x in FILE:
            line = ""
            for s in x:
                if s.isalpha():
                    if s.islower():
                        line = line + s.upper()
                    else:
                        line = line + s.lower()
                else:
                    line = line + s
            w.write(line)

