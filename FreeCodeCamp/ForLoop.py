#function 1
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print(f"{base} to the power of {exponent} is {result}.")

power(37, 4)  # Add your arguments here!

#Another Option:For Loop

def to_the_power(base, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base
    return result
print(to_the_power(2, 3))

#Nesting ForLoop
#ForLoop inside a ForLoop
Number_grid = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]
for row in Number_grid:
    for col in row:
        print(col)
