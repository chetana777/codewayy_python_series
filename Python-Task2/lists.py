#Working with methods of Lists:

#creating a list:
numbers = [25,69,78,35,24,69,12]
print("The list of numbers : ",numbers)


# 1)using append() method:
numbers.append(85)
print("\nThe list of numbers after using append method: ",numbers)


# 2)using insert() method:
numbers.insert(2,45)
print("\nThe list of numbers after using insert method: ",numbers)


# 3)using remove() method:
numbers.remove(69)
print("\nThe list of numbers after using remove method: ",numbers)


# 4)using pop() method:

#passing index in pop() method:
numbers.pop(4)
print("\nThe list of numbers after using pop method with index: ",numbers)

#without passing index in pop() method:
numbers.pop()
print("\nThe list of numbers after using pop method without index: ",numbers)


# 5)using extend() method:
numbers.extend([5,8,6])
print("\nThe list of numbers after using extend method: ",numbers)


# 6)using min() method:
numbers1=min(numbers)
print("\nThe minimum number from the list numbers is: ",numbers1)


# 7)using sum() method:
numbers2=sum(numbers)
print("\nThe sum of all elements in the list numbers is: ",numbers2)





