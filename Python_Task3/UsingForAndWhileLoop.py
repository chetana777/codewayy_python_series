#program to print all numbers till 10 except 3,7 usimg for loop and while loop:

#using for loop

def PrintNumbersUsingForLoop():
    for number in range (1,11):
        if number==3 or number==7:
            continue
        print(number,end=' ')
    print("\n")


#using while loop:

def PrintNumbersUsingForLoop():
    number=1
    while(number!=11):
        if number==3 or number==7:
            number+=1
        else:
            print(number,end=' ')
            number+=1
    print("\n")

        
#calling functions
print("Printing Numbers by using for loop")
PrintNumbersUsingForLoop()
print("Printing Numbers by using while loop")
PrintNumbersUsingForLoop()
        
