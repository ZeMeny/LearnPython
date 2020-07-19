#1
def same_first_last(nums):

  #Given an array of ints, return True if the array is length 1 or more, and the first element
  # and the last element are the same.

  return len(nums) > 0 and nums[0] == nums[-1]
#2
def middle_way(a, b):

  #Given 2 int arrays, a and b, each length 3, return a new array length 2
  #containing their middle elements.

  return [ a[1] , b[1] ]
