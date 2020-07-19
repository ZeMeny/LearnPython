
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = abc.upper()

# def Encry(abc):
#     key = {}
#     for letter in abc:
#         key[letter] = key(chr(ord(letter) + 13))
#     return key
# print(Encry(abc))


encrypt = input('enter a word to encrypt: ')
print(encrypt)
encrypt_length = len(encrypt)

encrypt_output = " "
for i in range(encrypt_length):
    character = encrypt[i]
    location_of_character = abc.find(character)
    new_location = location_of_character + 13
    encrypt_output += abc[new_location]

print(encrypt_output)




# print(encrypt_outputpt)
#
# decript = print(input('enter a word to decrypt: '))
# decript = decript.lower().replace(" ", "")
#
# for letter in decript:
#     print(chr(ord(letter) - 13))

