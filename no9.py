#oldest
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

if age1 >= age2 and age1 >= age3 and age1 >= age4:
    oldest_age = age1
elif age2 >= age1 and age2 >= age3 and age2 >= age4:
    oldest_age = age2
elif age3 >= age1 and age3 >= age2 and age3 >= age4:
    oldest_age = age3
else:
    oldest_age = age4

print(f"The oldest person is {oldest_age} years old.")