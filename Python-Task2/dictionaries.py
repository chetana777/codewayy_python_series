#Working with methods of Sets:


#creating a dictionary:
fruits = {"a":"Apple","b":"Banana","c":"Cherry","m":"Mango"}
print("The dictionary of fruits : ",fruits)


# 1)using get() method to get value:
get_fruit=fruits.get("m")
print("value for the 'm' key is: ",get_fruit)



# 2)using keys() method to get keys:
keys = fruits.keys()
print("keys: ",keys)


# 3)using len() method to find length:
length = len(fruits)
print("The length of the fruits dictionary is: ",length)


# 4)using values() method to get all the values:
values = fruits.values()
print("values: ",values)


# 5)using items() method to get all the items of dictionary:
items = fruits.items()
print("Items: ",items)



# 6)using pop() method to delete last element:
fruits.pop("c")
print("The fruits dictionary after performing a pop('c') opearation: ",fruits)


# 7)using copy() method to copy the given dictionary into another:
fruits_new = fruits.copy()
print("The new copy of fruits dictionary is: ",fruits_new)





