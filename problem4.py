def is_palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    else:
        return False


largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            if product > largest_palindrome:
                largest_palindrome = product
print(largest_palindrome)
