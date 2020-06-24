#Working with methods of Lists:

#creating a list:
numbers = [25,69,78,35,24,69,12]
print("The list of numbers : ",numbers)


# 1)using append() method to apend new element at the end of list:
numbers.append(85)
print("The list of numbers after using append method: ",numbers)


# 2)using insert() method to insert new element into list:
numbers.insert(2,45)
print("The list of numbers after using insert method: ",numbers)


# 3)using remove() method to remove element:
numbers.remove(69)
print("The list of numbers after using remove method: ",numbers)


# 4)using pop() method to delete last element:

#passing index in pop() method:
numbers.pop(4)
print("The list of numbers after using pop method with index: ",numbers)

#without passing index in pop() method:
numbers.pop()
print("The list of numbers after using pop method without index: ",numbers)


# 5)using extend() method to combine elements to the list:
numbers.extend([5,8,6])
print("The list of numbers after using extend method: ",numbers)


# 6)using min() method to get the minimum element:
numbers1=min(numbers)
print("The minimum number from the list numbers is: ",numbers1)


# 7)using sum() method to get sum of all elements:
numbers2=sum(numbers)
print("The sum of all elements in the list numbers is: ",numbers2)





