

def Reverse_string(s):                               # Define function
    indexStart = 0                                   # Initialize start index     
    indexEnd = len(s) - 1                            # Initialize end index
    while indexStart < indexEnd:                        
        s[indexStart],s[indexEnd] = s[indexEnd],s[indexStart]       # Swap characters at start and end
        indexStart += 1                             # Move start index to the right                                    
        indexEnd -= 1                               # Move end index to the left
    return s

input_array1 = ["h","e","l","l","o"]                # List of characters
input_array2 = ["H","a","n","n","a","h"]

Output1 = Reverse_string(input_array1)              # Call the function
Output2 = Reverse_string(input_array2)

print(Output1)                                      # Show the result
print(Output2)