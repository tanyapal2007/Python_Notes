num = int(input("Enter a number1"))
original = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //=10
print("Palindrome" if original==rev else"Not Palindrome")