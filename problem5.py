def smallest_multiple():
    step = 3 * 5 * 7 * 13 * 17 * 19
    for i in range(step, 1000000000**2, step):
        for j in range(1,21):
            if i % j == 0:
                if j == 20:
                    return i
                else:
                    continue
            else:
                break

print(smallest_multiple())