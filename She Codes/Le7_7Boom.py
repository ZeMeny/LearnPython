# create program that counts from 1 to 20 where any num divisible by 7 will be replace by "boom"
for number in range(1, 21):
    if number % 7 == 0 :
        print("Boom")
    else:
        print(number)
#
# def game():
#
#     count = 1
#     while count <= 21:
#         user_number = input('next number: ')
#         if count % 7 == 0 and user_number == "Boom":
#             count += 1
#         elif count % 7 != 0 and user_number == str(count):
#             count += 1
#         else:
#             print("not correct you lose")
#             break
#     return count
#
# print(game())

def seven_boom():

    count = 1
    while count <= 21:
        user_turn = True
        if user_turn:
            user_number = input('next number: ')
            if count % 7 == 0 and user_number == "Boom":
                count += 1
            elif count % 7 != 0 and user_number == str(count):
                count += 1
            else:
                print("not correct you lose")
                break
        else:
            if count % 7 == 0:
                 print("Computer say Boom")
                 break
            else:
                 print(f'computer say: {count}')
                 break

    return count

print(seven_boom())


