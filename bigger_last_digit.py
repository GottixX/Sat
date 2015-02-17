a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

last_digit1 = a % 10
last_digit2 = b % 10

if last_digit1 > last_digit2:
    print(a)
elif last_digit1 < last_digit2:
    print(b)
else:
    if a > b:
        print(a)
    else:
        print(b)
