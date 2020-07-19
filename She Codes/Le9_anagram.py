from collections import Counter

# the counter function allows you to count the items in an iterable list. so it check if the items
# (letters) exist in the string when the order doesnt matter.


# class Solution to see if the 2 strings are anagram:

def isanagram(s: str, t: str):

    return Counter(s) == Counter(t)


print(isanagram('run', 'nur'))