num = input("Enter a 4-digit number: ")

first = int(num[:2])
second = int(num[2:])

if first % 2 == 0:
    print(first, "is Even")
else:
    print(first, "is Odd")

if second % 2 == 0:
    print(second, "is Even")
else:
    print(second, "is Odd")

o/p:
Enter a 4-digit number: 4567
45 is Odd
67 is Odd
