n = input("Enter a number: ")
n = int(n)

nrev = n
revnum = 0

while n != 0:
    digit = n % 10

    revnum = revnum * 10 + digit

    n = n // 10

if nrev == revnum:
    print(str(nrev) + " is a palindrom")
else:
    print(str(nrev) + " is not a palindrom")
