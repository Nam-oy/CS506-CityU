def find_unique(arr):  # Define the function
    unique_value = set()  # Define unique_value as a set to store unique values (no duplicates)

    for d in arr:  # Loop1: Iterate over each dictionary in the list
        for value in d.values():  # Loop2: Get each value from the current dictionary
            unique_value.add(value)  # Add the value to the set (duplicates are automatically ignored)
    
    return unique_value  # Return the set of unique values



# Test case
dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]  # Define list of dictionaries
new_dic = find_unique(dic)  # Call the function to find unique values

# Print the result
print("Sample Data:", dic)
print("Expected Output: Unique Values:", new_dic)
