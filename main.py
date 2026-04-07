def main() -> None:
    print("Hello python", "From Mohit Jogiwala")

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

if __name__ == "__main__":
    main()
    greet("Mohit")
    print("Addition", add(2,3))
    print("Sum of all numbers", sum_all(1,2,3,4))
    print_user(name="Mohit", age=26, city="Surat")