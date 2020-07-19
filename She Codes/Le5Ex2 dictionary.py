#def char_freq(dictionary):
    #freq = {}
    #for letter in dictionary:
       # freq[letter] = freq.get(letter, 0) + 1
    #return freq
#print(input(f"enter a word: {freq} "))

str1 = input("enter a word: ")

my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)





