import time

def collatz_len(num):
    current_num = num
    chain_len = 1
    while current_num != 1:
        if current_num % 2 == 0:
            chain_len += 1
            current_num /= 2
        else:
            chain_len += 1
            current_num = current_num * 3 + 1
    return chain_len


def problem14():
    largest_len = 0
    largest = None
    for i in range(1, 1000001):
        if i % 10000 == 0:
            print(i, " ", largest_len)
        current = collatz_len(i)
        if current > largest_len:
            largest_len = current
            largest = i
        else:
            continue
    return largest

current_time = time.perf_counter()
print(problem14())
duration = time.perf_counter() - current_time
print(duration)