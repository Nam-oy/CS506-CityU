
def Add_Digits(num):                            # Define function
    while num >= 9:                             # Loop1: Check digits more than one digit
        sum_num = 0                             # Create varlible to store for sum of digits
        while (num > 0):                            # Loop2: runs while num is greater than 0                                        
            sum_num += num % 10                         # Add the last digit of num to sum_num
            num //= 10                                  # Remove the last digit from num by doing integer division
        num = sum_num                               # Set num to the sum of its digits
    return num

num = int(input())                              #Get User input
Output = Add_Digits(num)                        #Call the function
print ("Input : ", num, "Output :", Output )    #Show the result


