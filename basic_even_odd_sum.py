# ---- QUESTION ----

# Given an array Arr[] of N integers, write a program to find the sum of values of even and odd index positions separately.

# Input: 
# First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a single integer N which denotes the number of elements in the array. Second line of each test case contains N space separated integer which denotes the elements of the array.
# Output:
# For each test case, in first line print the sum of elements of array present at even indexes and in the second line print the sum of elements at odd indexes.

# Constraints:
# 1<=T<=100
# 1<=N<=1000
# 1<=Arr[i]<=105

# Example:
# Input:
# 2
# 6
# 1 2 3 4 5 6
# 7
# 10 20 30 40 50 60 70
# Output:
# 9
# 12
# 160
# 120

# ---- ANSWER ----

# NOTE: this is the functional solution
# this would be more performant (and arguably simpler) using a single loop
# this could also be written more elegantly in javascript with just filter and reduce
def basic_even_odd(numbers_array):
	even_indexes = filter(lambda x: x % 2 == 0, range(len(numbers_array)))
	odd_indexes = filter(lambda x: x % 2 == 1, range(len(numbers_array)))
	print(sum([numbers_array[i] for i in even_indexes]))
	print(sum([numbers_array[i] for i in odd_indexes]))

basic_even_odd([0, 1, 0, 2])
