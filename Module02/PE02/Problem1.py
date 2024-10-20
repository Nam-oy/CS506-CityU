def Check_arr(arr): #Define function
    for i in range(len(arr)): #Loop1: iterate over all elements in the array
        for j in range(len(arr)): #Loop2: compare each of others element in the array
            if i != j and arr[i] == 2 * arr[j]: # Check if the indices are different and if one value is double the other
                return True  # Return True if a pair is found
    return False # Return False if no such pair is found

     
#Test cases  
Array1 = [10, 2, 5, 3] # Define Array1
ToCheck1 = Check_arr(Array1) # Call the function
print("Input: arr = ", Array1,"Output:", str(ToCheck1)) #Show the result

Array2 = [7, 1, 14, 11] #Define Array2
ToCheck2 = Check_arr(Array2) # Call the function
print("Input: arr = ", Array2,"Output:", str(ToCheck2)) #Show the result

Array3 = [3, 1, 7, 11] #Define Array2
ToCheck3 = Check_arr(Array3) # Call the function
print("Input: arr = ", Array3,"Output:", str(ToCheck3)) #Show the result