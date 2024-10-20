# Digital Root=1+(num−1)%9
def addDigits(num):
    if num == 0:
        return 0   # Special case for 0
    return 1 + (num - 1) % 9   # Calculate the digital root 
                               # following formula:


num = int(input())          #Get User input
Formula = addDigits(num)    # Call the function
print ("Formula : ",Formula )   # Show the result
