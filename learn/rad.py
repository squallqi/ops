#!/usr/bin/env python
import random
import sys
a = []
for i in range(6):
    if i == random.randint(1,9):
        a.append(str(random.randint(1,9)))
    else:
        temp = random.randint(64,90)
        a.append(chr(temp))
print ''.join(a)

