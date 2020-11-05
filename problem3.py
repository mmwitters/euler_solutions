x = 600851475143
max = 2

while x != 1:
    if x % max == 0:
        x /= max
    else:
        max += 1
print(max)
