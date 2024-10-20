def Sort_tuples(arr):  # Define the function
    sorted_by_second = sorted(arr, key=lambda x: x[1])  # Sort using the second element of each tuple
    return sorted_by_second #Return the result


Array1 = [('452', 10), ('256', 5), ('100', 20), ('135', 15)] # Define the input list of tuples
SortArray = Sort_tuples(Array1)# Call the function to sort the array
print("Input :", Array1)  # Print the input list of tuples
print("Output :", SortArray)  # Print the sorted list of tuples

