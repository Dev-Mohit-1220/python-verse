from functions import add, sum_all, print_user, greet, square, is_even, filter_even
from control_flow import check_number, max_number, grade, print_numbers, sum_n, count_down

def main() -> None:
    print("Hello python", "From Mohit Jogiwala")
    greet("Mohit")
    print("Addition", add(2,3))
    print("Sum of all numbers", sum_all(1,2,3,4))
    print_user(name="Mohit", age=26, city="Surat")
    print("Square", square(6))
    print("Even", is_even(25))
    print("Filter even no", filter_even([1,2,3,4,5,6]))
    check_number(1)
    print("Max number", max_number(1,2,3,4,5))
    print("Grade", grade(105))
    print("Total",sum_n(20))
    count_down(100000)

if __name__ == "__main__":
    main()
