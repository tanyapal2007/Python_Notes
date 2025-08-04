number = [1,2,3,4,5,6,7,8,9,10]
even = 0
odd = 0

for n in number:
    if n % 2 == 0:
        print(n)
        even += 1
    
    else:
        print(n)
        odd += 1

print("Even" ,even, "Odd" ,odd)