n = input("Enter number: ")
n = int(n)

tot = 0

while n != 0:
    digit = n % 10
   
    tot += digit
    
    n = n // 10

print("Sum of digits is: " + str(tot))
