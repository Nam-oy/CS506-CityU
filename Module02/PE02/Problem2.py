def Remove_Dup(arr): #Define the function
    if not arr: #Check if the array is empty 
        return 0 #Return 0 if the array is empty
    
    i = 0 # create the pointer to track unique element

    for j in range(1,len(arr)): #Loop: j starts from index1(second element) to the end of the array
        if arr[j]!= arr[i]:# Check if the current element is different from the last unique element
            i += 1 #Move the pointer to the next position
            arr[i] = arr[j]  # Assign the unique element to the next correct position
            
    return i + 1 #return the new length of array, +1 because 'i' is zero-based indexing
    

#Test cases
Array1 = [1,1,2] #Define Array1
NewA1 = Remove_Dup(Array1) #Call the function
print("Your function should return length = ",NewA1, "with the first two elements of nums being",Array1[:NewA1]) #Show the result

Array2 = [0,0,1,1,1,2,2,3,3,4] #Define Array2
NewA2 = Remove_Dup(Array2) #Call the function
print("Your function should return length = ",NewA2, "with the first two elements of nums being",Array2[:NewA2]) #Show the result