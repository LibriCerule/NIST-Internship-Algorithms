#!/usr/bin/python2
import sys

with open(sys.argv[1], "r") as FILE:
    with open('out.txt', 'w') as w:
        for x in FILE:
            line = ""
            for s in x:
                if s == 'm':
                    line = line + 'M'
                elif s == 'M':
                    line = line + 'm'
                else:
                    line = line + s
            w.write(line)

