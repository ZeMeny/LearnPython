#triangle shape
num1 = int(input("enter number of rows: "))
for i in range(0, num1):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#trapeze shape:
num2 = int(input("enter number of rows: "))
for i in range(0, num2):
    for j in range(i + 4):
        print("*", end=" ")
    print()

#diamond shape:
num3 = 5
for i in range(0, num3):
    if i == 0:
        for j in range(i + 1):
            print("   ", "*", end=" ")
    elif i == 1:
        for j in range(i+1):
            print(" ", "*", end=" ")
    elif i == 2:
        print("*", " ", "*", " ", "*", end=" ")
    elif i == 3:
        for j in range(i-1):
            print(" ", "*", end=" ")
    else:
        for j in range(i-3):
            print("   ", "*", end=" ")

    print()




#     stars = " "
#     for number in numbers:
#         stars += "*"
#     return stars
# numbers = 1
# print(print_stars(numbers)