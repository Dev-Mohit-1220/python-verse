def sqaure_pattern(num: int) -> None:
    for i in range(num):
        for j in range(num):
            print("*", end ="")
        print()

def print_num_in_rows(num: int) -> None:
    for i in range(num):
        for j in range(num):
            print(j+1, end ="")
        print()

def multiplication_pattern(num: int) -> None:
    for i in range(num):
        for j in range(num):
            print((i+1)*(j+1), end ="")
        print()

def right_triangle_pattern(num: int) -> None:
    for i in range(num+1):
        for j in range(i):
            print("*", end="")
        print()

def reverse_pattern(num: int) -> None:
    for i in range((num+1),0, -1):
        for j in range(i):
            print("*", end="")
        print()

def number_triangle(num: int) -> None:
    for i in range(0, num+1):
        for j in range (i):
            print(j+1, end ="")
        print()

def floyd_triangle(num: int) -> None:
    counter: int = 0
    for i in range(0, num+1):
        for j in range (i):
            counter += 1
            print(counter , " ",end ="")
        print()

def pyramid_triangle(num: int) -> None:
    for i in range(1, num+1):
        for j in range(num-i):
            print("#", " ",end="")

        for k in range(2 * i -1):
            print("*", " ",end="")
        print()