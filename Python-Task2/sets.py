#Working with methods of Sets:


#creating a set:
colors = {"black","white","pink","blue"}
print("The set of colors : ",colors)


# 1)using add() method:
colors.add("red")
print("\ncolors set after adding a color: ",colors)


# 2)using update() method:
colors.update(["magenta","green"])
print("\ncolor set after updation: ",colors)


# 3)using length() method:
length = len(colors)
print("\nThe length of the colors set is: ",length)


# 4)using remove() method:
colors.remove("blue")
print("\nThe colors set after removing blue color: ",colors)



# 5)using discard() method:
colors.discard("green")
print("\nThe colors set after discarding green color: ",colors)



# 6)using pop() method:
colors.pop()
print("\nThe colors set after performing a pop opearation: ",colors)


# 7)using clear() method:
colors.clear()
print("\nThe set colors after using clear method: ",colors)





