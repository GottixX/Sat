n = input("Enter a number: ")
n = int(n)

revnum = 0

while n != 0:
    digit = n % 10

    revnum = revnum * 10 + digit

    n = n // 10

print("The reversed number is: " + str(revnum))
