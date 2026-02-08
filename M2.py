# Numeric variables
hours_worked = 40
hourly_rate = 22.50
bonus = 150

# Arithmetic operations
weekly_pay = hours_worked * hourly_rate
total_pay = weekly_pay + bonus

print(f"I worked {hours_worked} hours this week at ${hourly_rate} per hour.")
print(f"My weekly pay before bonus is ${weekly_pay}.")
print(f"After adding a bonus of ${bonus}, my total pay is ${total_pay}.")

# String variable and manipulation
first_name = "Derek"
last_name = "Kissoon"

full_name = first_name + " " + last_name
initials = first_name[0] + last_name[0]

print(f"My full name is {full_name}.")
print(f"My initials are {initials}.")

# Boolean expression
overtime_eligible = hours_worked > 40

print(f"Did I work overtime this week? {overtime_eligible}")
