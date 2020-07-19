# a function that gets a list of strings and
# returns the strings whose first and last characters match
def same_first_last(name_list):
    new_list = []
    for element in name_list:
        if len(element) > 1 and (element[0] == element[-1]):
            new_list.append(element)
    return new_list


name_list = ["abba", "noa", "hey", "oho"]
print(same_first_last(name_list))
