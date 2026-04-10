def check_number(num: int) -> None:
    if(num > 0):
        print("Positive number")
    elif(num < 0):
        print("Negative number")
    else:
        print("Number is zero")

def max_number(*nums: int) -> int:
    return max(nums)

def grade(mark: int) -> int:
    return "A" if mark >= 90 else \
           "B" if mark >= 75 else \
           "C" if mark >= 50 else \
           "Fail"

def print_numbers(value: int) -> None:
    for i in range(1, value+1 ):
        print(i)

def sum_n(value: int) -> int:
    total = 0
    for i in range(1, value + 1):
        total += i
    return total

def count_down(value: int) -> None:
    while value > 0:
        print (value)
        value -= 1

def odd_nums(value: int) -> None:
    for i in range(1, value):
        if(i%2 == 0):
            continue
        print(i)

def star_pattern(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)