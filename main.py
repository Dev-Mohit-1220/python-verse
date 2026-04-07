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

if __name__ == "__main__":
    main()
    greet("Mohit")
    print("Addition", add(2,3))
    print("Sum of all numbers", sum_all(1,2,3,4))