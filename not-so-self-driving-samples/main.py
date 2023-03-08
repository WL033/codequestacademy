import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
t = []
for caseNum in range(cases):
    current = sys.stdin.readline().rstrip()
    v = float(current[0: current.index(":")])
    d = float(current[current.index(":")+1:])
    if(v != 0 and d != 0):
        t.append(d/v)
    else:
        t.append(-1)

for element in t:

    if element <= 1 and element != -1:
        print("SWERVE")
    elif element <= 5 and element != -1:
        print("BRAKE")
    else:
        print("SAFE")
