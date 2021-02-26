from math import sqrt

prime_list = []
start_num = 2


def is_prime(prime_list, number):
    for prime in prime_list:
        if prime > sqrt(number):
            return True
        if number % prime == 0:
            return False
    return True


while len(prime_list) < 10_002:
    if is_prime(prime_list, start_num):
        prime_list.append(start_num)
    start_num += 1

print(prime_list[10_000])
