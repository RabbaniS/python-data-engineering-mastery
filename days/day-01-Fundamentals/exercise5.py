#Annual salary calculator
monthly_salary=float(input("Enter your monthly salary: "))
annual_salary=monthly_salary*12
print(f"Your annual salary is: {annual_salary}")

#Swap two numbers without using a temporary variable
a=25
b=50
print(f"Before swapping: a={a}, b={b}")
a,b=b,a
print(f"After swapping: a={a}, b={b}")

#calulate the percentage of marks obtained by a student
telugu=80
hindi=75
english=90
total_marks=telugu+hindi+english
percentage=(total_marks/300)*100
print(f"Percentage of marks obtained: {percentage}%")

#Calculate the final salary of an employee after a 10% increment
basic_salary=50000
bonus=10
final_salary=basic_salary+(basic_salary*bonus/100)
print(f"Final salary after 10% increment: {final_salary}")