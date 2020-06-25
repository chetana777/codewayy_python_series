#function for displaying full name:

def FullName():
    FullName=input("enter your FullName=>")
    print("My Name is =>",FullName)


#function for returning total marks:

def CalculateTotalMarks():
    
#creating an empty list:
    Marks=[]

#number of elements as input:
    NumberOfSubjects=int(input("enter number of subjects=>"))

    for i in range(0,NumberOfSubjects):
        SubjectMarks=int(input("Enter marks:"))
        Marks.append(SubjectMarks)

    TotalMarks=sum(Marks)
    print("Total marks are=>",TotalMarks)

#function for returning percentage:

def CalculatePercentage():
    TotalMarks=int(input("enter total marks=>"))
    NumberOfSubjects=int(input("enter number of subjects=>"))
    Percentage=TotalMarks/NumberOfSubjects
    print("Percentage=>",Percentage)

#function for displaying Grades:

def CalculateGrades():
    Percentage=float(input("enter total percentage=>"))
    if (Percentage>=95):
        print("Obtained Grade is A")
    elif (Percentage>=85 and Percentage<=95):
        print("Obtained Grade is B")
    elif (Percentage>=75 and Percentage<=85):
        print("Obtained Grade is C")
    elif (Percentage>=65 and Percentage<=55):
        print("Obtained Grade is D")
    else:
        print("OOPs you are Failed")

#function to print mydetails:
    
def MyDetails():
    FullName()
    CalculateTotalMarks()
    CalculatePercentage()
    CalculateGrades()

#calling function MyDetails
    
MyDetails()




