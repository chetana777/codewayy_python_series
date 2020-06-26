#function for displaying full name:

def fullName():
    fullName=input("enter your FullName=>")
    print("My Name is =>",fullName)


#function for returning total marks:

def calculateTotalMarks():
    
#creating an empty list:
    Marks=[]

#number of elements as input:
    numberOfSubjects=int(input("enter number of subjects=>"))

    for i in range(0,numberOfSubjects):
        subjectMarks=int(input("Enter marks:"))
        Marks.append(subjectMarks)

    totalMarks=sum(Marks)
    print("Total marks are=>",totalMarks)

#function for returning percentage:

def calculatePercentage():
    totalMarks=int(input("enter total marks=>"))
    numberOfSubjects=int(input("enter number of subjects=>"))
    percentage=totalMarks/numberOfSubjects
    print("Percentage=>",percentage)

#function for displaying Grades:

def calculateGrades():
    percentage=float(input("enter total percentage=>"))
    if (percentage>=95):
        print("Obtained Grade is A")
    elif (percentage>=85 and percentage<=95):
        print("Obtained Grade is B")
    elif (percentage>=75 and percentage<=85):
        print("Obtained Grade is C")
    elif (percentage>=65 and percentage<=55):
        print("Obtained Grade is D")
    else:
        print("OOPs you are Failed")

#function to print mydetails:
    
def myDetails():
    fullName()
    calculateTotalMarks()
    calculatePercentage()
    calculateGrades()

#calling function MyDetails
    
myDetails()




