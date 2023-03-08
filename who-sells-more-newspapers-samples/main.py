import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    current = sys.stdin.readline().rstrip()
    t = int(current[0:current.index(" ")])
    h = int(current[current.index(" "):])
    if t > h:
        print("Times has", t-h, "more subscribers")
    elif h > t:
        print("Herald has", h-t, "more subscribers")
    else: print("Times and Herald have the same number of subscribers")