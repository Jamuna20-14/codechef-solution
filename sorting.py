size = int(input("Enter size: "))

numbers = []

for i in range(size):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Ascending Order:")
for num in numbers:
    print(num, end=" ")
