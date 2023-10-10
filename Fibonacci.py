n = int(input("Enter number of elements of the series you want : "))
ctr = 1
sum = 0
i = 1
temp = 0

print("Your Fibonacci series is upto", n, "is : ")

while ctr <= n:
    print(sum, end=" ")
    temp = i
    i = sum
    sum = temp + i
    ctr += 1
