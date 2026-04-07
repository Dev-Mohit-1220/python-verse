from functions import add, sum_all, print_user, greet, square

def main() -> None:
    print("Hello python", "From Mohit Jogiwala")
    greet("Mohit")
    print("Addition", add(2,3))
    print("Sum of all numbers", sum_all(1,2,3,4))
    print_user(name="Mohit", age=26, city="Surat")
    print("Square", square(6))

if __name__ == "__main__":
    main()
    