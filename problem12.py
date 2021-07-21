from collections import Counter
import time


def prime_factors(num):
    prime_factors = Counter()
    start = 2
    current = num
    while current > 1:
        if current % start == 0:
            prime_factors[start] += 1
            current = current / start
        else:
            start += 1
    return prime_factors


def num_of_factors(num):
    count = prime_factors(num)
    fac_num = 1
    for prime, exponent in count.items():
        fac_num *= exponent + 1
    return fac_num


def problem12():
    current = 1
    for i in range(2, 20000000000000):
        current += i
        factors = num_of_factors(current)
        if factors >= 500:
            return current


if __name__ == "__main__":
    start = time.perf_counter()
    print(problem12())
    total = time.perf_counter() - start
    print("Total Time: ", total)
