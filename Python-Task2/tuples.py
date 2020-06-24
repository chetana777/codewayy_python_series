#Working with methods of Tuple:
#Note : Tuples are Immutable.

#creating a tuple:
numbers = (25,69,78,35,24,69,12,78)
print("The tuple of numbers : ",numbers)


# 1)using count() method to count how many times the element is present in the tuple:
count = numbers.count(78)
print("The occurence of 78 in the numbers tuple is: ",count)


# 2)using index() method to find index:
index = numbers.index(69)
print("The index of 69 is: ",index)


# 3)using length() method to get length:
length = len(numbers)
print("The length of the numbers tuple is: ",length)


# 4)using max() method to get maximum element:
maximum_number = max(numbers)
print("The maximum number of the numbers tuple is: ",maximum_number)



# 5)using min() method to get minimum element:
minimum_number = min(numbers)
print("The minimum number of the numbers tuple is: ",minimum_number)



# 6)using sum() method to calculate sum:
summation =sum (numbers)
print("The sum of all elements in the tuple numbers is: ",summation)


# 7)conversion of list to tuple:
list = [1,2,3,4]
Tuple = tuple(list)
print("The tuple obtained by converting a list into tuple is: ",Tuple)





