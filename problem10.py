from math import sqrt

prime_list = []


def is_prime(prime_list, number):
    for prime in prime_list:
        if prime > sqrt(number):
            return True
        if number % prime == 0:
            return False
    return True


for i in range(2, 2_000_000):
    if is_prime(prime_list, i):
        prime_list.append(i)

print(sum(prime_list))
