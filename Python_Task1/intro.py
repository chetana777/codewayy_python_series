#program for display full name, college name, address, marks total and percentage.


#Declaring variables:
First_name = "Chetana "
Middle_name = "Suresh "
Last_name = "Tijare"
College_name = "Yeshwantrao Chavan College Of Engineering, Nagpur. "
Address = "Paradsinga, Maharashtra "
Marks_Artificial_Intelligence = 80
Marks_Web_Devlopment = 85
Marks_Operating_Systems = 78
Marks_Computer_Networks = 83
Marks_Software_Engineering = 86


#Concate strings to get Full name:
Full_name = First_name + Middle_name + Last_name


#printing full name:
print("My Name is ",Full_name)


#Concate strings to get college name and adress:
College_and_Address = (College_name + "My Address is " + Address)


#printing college name and address:
print("\nI am Pursuing BE in IT from ",College_and_Address)

#printing marks obtained
print("\nMarks Obtained:")
print("Artificial_Intelligence",Marks_Artificial_Intelligence)
print("Web_Devlopment",Marks_Web_Devlopment)
print("Operating_Systems",Marks_Operating_Systems)
print("Computer_Networks",Marks_Computer_Networks)
print("Software_Engineering",Marks_Software_Engineering)


#printing total marks:
Total_marks = Marks_Artificial_Intelligence + Marks_Web_Devlopment + Marks_Operating_Systems + Marks_Computer_Networks + Marks_Software_Engineering
print("\nTotal Marks is : ",Total_marks)


#calculating percentage:
percentage = round((Total_marks/500)*100)
Percentage = "{}% ".format(percentage)
print("\nTotal Percentage is: ",Percentage)


