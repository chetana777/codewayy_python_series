#Working with methods of Sets:


#creating a dictionary:
fruits = {"a":"Apple","b":"Banana","c":"Cherry","m":"Mango"}
print("The dictionary of fruits : ",fruits)


# 1)using get() method:
get_fruit=fruits.get("m")
print("\nvalue for the 'm' key is: ",get_fruit)



# 2)using keys() method:
keys = fruits.keys()
print("\nkeys: ",keys)


# 3)using length method:
length = len(fruits)
print("\nThe length of the fruits dictionary is: ",length)


# 4)using values()method:
values = fruits.values()
print("\nkeys: ",values)


# 5)using items() method:
items = fruits.items()
print("\nItems: ",items)



# 6)using pop() method:
fruits.pop("c")
print("\nThe fruits dictionary after performing a pop('c') opearation: ",fruits)


# 7)using copy() method:
fruits_new = fruits.copy()
print("\nThe new copy of fruits dictionary is: ",fruits_new)





