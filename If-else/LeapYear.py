year = int(input("Enter the Year = "))

if year%400==0:
    print("Leap Year")
elif year%100==0:
    print("Enter a valid Leap Year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")

