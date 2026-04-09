def greet(name: str = "Guest") -> None:
    print("Hello", name)

def add(a: int, b: int) -> int:
    return a+b

def sum_all(*nums: int) -> int:
    total: int = 0
    for n in nums:
        total += n
    return total

def print_user(**data: str) -> None:
    for key, value in data.items():
        print(key, value)

def is_even(num: int) -> bool:
    return num % 2 == 0

def filter_even(nums: list[int]) -> list[int]:
    return [n for n in nums if n % 2 == 0]

square = lambda x: x * x