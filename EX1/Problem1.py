
def Reduced_to_Zero(num):       # Define function
    Output = 0                  # To count the number of the steps
    while num > 0:              # Loop to reduced to zero
        if (num % 2) != 0:      # Check odd and even --if odd -> subtract 1 -> Increment step counter
            num = num - 1
            Output += 1         
        else:                   # -- else -> even -> Increment step counter
            num = num // 2
            Output += 1         
    return Output


num = int(input())              #Get User input
step = Reduced_to_Zero(num)     #Call the function
print ("Input: ",num,"Output: ",step) #Show the result