#function 1
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print(f"{base} to the power of {exponent} is {result}.")

power(37, 4)  # Add your arguments here!

#function 2
def cube(number):
  cube = number * number * number
  return cube
def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False