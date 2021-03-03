from math import sqrt

def pythagtrip():
    for a in range(500):
        for b in range(500):
            c = sqrt(a**2 + b**2)
            if int(c) != c:
                continue
            else:
                if a + b + c == 1000:
                    result = a*b*c
                    return int(result)
                else:
                    continue

print(pythagtrip())
