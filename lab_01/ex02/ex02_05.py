hours = float(input("Enter working hours: "))
wage = float(input("Enter hourly wage: "))

if hours <= 44:
    salary = hours * wage
else:
    normal_salary = 44 * wage
    overtime_hours = hours - 44
    overtime_salary = overtime_hours * wage * 1.5
    salary = normal_salary + overtime_salary

print("Salary =", salary)