#Working with methods of Tuple:
#Note : Tuples are Immutable.

#creating a tuple:
numbers = (25,69,78,35,24,69,12,78)
print("The tuple of numbers : ",numbers)


# 1)using count() method:
count = numbers.count(78)
print("\nThe occurence of 78 in the numbers tuple is: ",count)


# 2)using index() method:
index = numbers.index(69)
print("\nThe index of 69 is: ",index)


# 3)using length() method:
length = len(numbers)
print("\nThe length of the numbers tuple is: ",length)


# 4)using max() method:
maximum_number = max(numbers)
print("\nThe maximum number of the numbers tuple is: ",maximum_number)



# 5)using min() method:
minimum_number = min(numbers)
print("\nThe minimum number of the numbers tuple is: ",minimum_number)



# 6)using sum() method:
summation =sum (numbers)
print("\nThe sum of all elements in the tuple numbers is: ",summation)


# 7)conversion of list to tuple:
list = [1,2,3,4]
Tuple = tuple(list)
print("\nThe tuple obtained by converting a list into tuple is: ",Tuple)





