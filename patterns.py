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