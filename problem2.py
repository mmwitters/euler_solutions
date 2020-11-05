a = 1
b = 1
result = 0
while b < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        result += c
print(result)
