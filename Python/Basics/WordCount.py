'''
Example form: https://new.pythonforengineers.com/blog/create-a-word-counter-in-python/
uses birds.txt

Objective: enter file name in arguments diplay number of words and lines in file
Learning: intro to sys.argv
'''

import sys

def word_count(data):
    words = data.split()
    return len(words)


def line_count(data):
    lines = data.split('\n')
    for l in lines:
        if not l:
            lines.remove(l)
    return len(lines)


f = open(sys.argv[1], "r") #sys.argv gives a list of arguments in command line
data = f.read()
f.close()

print('number of words:', word_count(data))
print('number of line:', line_count(data))




