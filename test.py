__author__ = 'jet'
import sys
import os

import re

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(p.sub(r'\2 \1', s))

st = 'abc\r\nFirstPage '
# r = re.compile(r'\b(([A-Z]+[a-z]+){2,})\b')
r = re.compile(r'\b((\w+){,3})\b')
test1 = '\r\nbc!df!'
test1_r = re.compile(r'\b(\w+)\b')
re1 = test1_r.search(test1)
re3 = test1_r.sub(r'test\1test', test1)
test2 = ''
re2 = r.findall(st)
content = r.sub(r'\0', st)

print('123')


