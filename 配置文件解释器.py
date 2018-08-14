# written by Zachary WU
# question 5

from sys import argv
import re

with open(argv[1],'r') as file:
    for line in file:
        if line[0] == '#':
            continue
        else:
            checkComment = line.find('#')
            if checkComment != -1:
                string = line[0:checkComment]
            else:
                string = line
            string = string.strip()
            data = string.split('=')
            print('{} {}'.format(data[0].strip(),data[1].strip()))
