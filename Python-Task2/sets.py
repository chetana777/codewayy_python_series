#Working with methods of Sets:


#creating a set:
colors = {"black","white","pink","blue"}
print("The set of colors : ",colors)


# 1)using add() method to add element:
colors.add("red")
print("colors set after adding a color: ",colors)


# 2)using update() method to update new element:
colors.update(["magenta","green"])
print("color set after updation: ",colors)


# 3)using length() method to get length:
length = len(colors)
print("The length of the colors set is: ",length)


# 4)using remove() method to remove element:
colors.remove("blue")
print("The colors set after removing blue color: ",colors)



# 5)using discard() method to delete element:
colors.discard("green")
print("The colors set after discarding green color: ",colors)



# 6)using pop() method to delete last element:
colors.pop()
print("The colors set after performing a pop opearation: ",colors)


# 7)using clear() method to clear all the set:
colors.clear()
print("The set colors after using clear method: ",colors)





