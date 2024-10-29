# factorial of first n numbers

n = int(input("write a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("factorial of this number is: ", fact)
