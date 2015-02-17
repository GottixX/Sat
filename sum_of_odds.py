n = input("Enter n: ")
n = int(n)

total = 0
a = 1

while a <= n:
    if a % 2 == 1:
        total += a
    a += 1
print("The sum is: " + str(total))
