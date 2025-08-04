n = int(input("How many numbers: "))
i = 0
total = 0
while i < n:
    num = float(input("Enter number: "))
    total += num
    i += 1
print("Average:", total / n)
