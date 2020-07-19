movie = ['the notebook', 'Maleficent', 'Batman vs Superman', 'Black Swan']
actor = ['Rachel Mcadams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman']

# Ex 1 create a one line code of a new list that will concatenate the 2 lists above with "is played by"
print([(movie[i] + " is played by " + actor[i]) for i in range(0, len(movie))])
# Ex 2 creat a dictionary with the 2 lists called movies:
movies = dict(zip(movie, actor))
print(movies)
# Ex 3 create a one line code of a new list from the movies dictionary above with "is played by":

print([key + " is played by " + value for (key, value) in movies.items()])

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = ['a', 'b', 'c', 'd', 'e']

print({my_list_1[x]: my_list_2[x] for x in range(len(my_list_2)) if x != 4})

# Ex 4 create a list that includes each number from 1-9 multiplied by 100 only if it divisible by 2,
print([x * 100 for x in range(1, 10) if x % 2 == 0])



# Ex 5 create a list that includes each number from 1-9 multiplied by 100 only if it divisible by 2, else return the number

print([x * 100 if x % 2 == 0 else x for x in range(1, 10)])
#another wat to see it

num_list = []
for x in range(1, 10):
    if x % 2 == 0:
        num_list.append(x * 100)
    else:
        num_list.append(x)
print(num_list)

# Ex 6 create a list from 1 to 99 where any num divisible by 7 will be replace by "boom"
print(["boom" if x % 7 == 0 else x for x in range(1, 100)])

# create a square list using lambda
print(list(map(lambda x : x ** 2, [1, 2, 3, 4, 5] )))

#Ex 7 write a code that returns the sum of 2 numbers

sum = lambda x, y: x + y
print(sum(3, 4))

#Ex 8 write a code the lists all the 36 combination of (1,1) to (6, 6)
print([(i, j) for i in range(1, 7) for j in range(1, 7)])

#ex 9 write a code that lists any value of Joules to kilocalories
joules = [5000, 8000, 10000, 6000, 12000]
print(list(zip(joules, map(lambda x: x / 4181, joules))))

#another version
print([(j, cal) for (j, cal) in zip(joules,[j / 4181 for j in joules])])

#Ex 10 use filter and lambda to filter out only Python language

languages = ['HTML', 'JavaScript', 'Python', 'Ruby']
print(list(filter(lambda i: i == 'Python', languages)))

#another version:
print([x for x in languages if x == 'Python'])

