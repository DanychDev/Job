import numpy as np
import sys


c = sys.argv[1]
with open(c, 'r') as f:
    d = f.read().splitlines()

a = list(map(int, d))

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

p = np.percentile(a, 90)
b = np.percentile(a, 50)

print (toFixed(p, 2))
print (toFixed(b, 2))
print (toFixed(max(a), 2))
print (toFixed(min(a), 2))
print(toFixed(sum(a) / len(a), 2))
