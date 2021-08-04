number_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen",
               20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
               90: "ninety"}


def ones_digit(num):
    return number_dict.get(num)


def tens_digit(num):
    if num < 20 or num % 10 == 0:
        return number_dict.get(num)
    else:
        num_str = str(num)
        return number_dict.get(int((num_str[0] + "0"))) + ones_digit(int(num_str[1]))


def hundreds_digit(num):
    num_str = str(num)
    if num % 100 == 0:
        return ones_digit((int(num_str[0]))) + "hundred"
    elif num_str[1] == "0":
        return ones_digit((int(num_str[0]))) + "hundredand" + ones_digit(int(num_str[2]))
    else:
        return ones_digit((int(num_str[0]))) + "hundredand" + tens_digit((int(num_str[1:])))


def translate_number(num):
    if num < 10:
        return ones_digit(num)
    elif num < 100:
        return tens_digit(num)
    elif num < 1000:
        return hundreds_digit(num)
    else:
        return "onethousand"


def problem17(max_num):
    char_count = 0
    for i in range(1, max_num + 1):
        translation = str(translate_number(i))
        print(translation)
        char_count += len(translation)
    return char_count


print(problem17(1000))
