def plusOne(digits):
    # By using "".join() module we are making the list into a string of "123"
    # and then turning the 123 string to an integer so we can then add +1 to the number.
    # returning it into a string and looping through the string to create a  new list

    return [int(n) for n in str(int("".join([str(d) for d in digits])) + 1)]


print(plusOne([1, 2, 3]))
