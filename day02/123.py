#!/usr/bin/python3.5
# Author: xiaojie
import re
s = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'

# res = re.findall(r'(?P<g1>[a-z]+)\d+(?P=g1)',s)
res = re.findall(r'(?P<g1>[a-z]+)',s)

print(res)
