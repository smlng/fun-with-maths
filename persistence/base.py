import sys

base = 16
maxnum = 100

if len(sys.argv) > 1:
    base = int(sys.argv[1])
if len(sys.argv) > 2:
    maxnum = int(sys.argv[2])


def base10to(base, number):
    remain = []
    j = number
    while j > 0:
        r = j % base
        if r > 9:
            r = chr(ord('A') + (r - 10))
        else:
            r = str(r)
        remain.append(r)
        j = int(j /base)
    return ''.join(x for x in remain[::-1])

for i in range(maxnum):
    print("b10: " + str(i) + " b"+str(base)+": " + base10to(base, i))
