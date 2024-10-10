def Reverse_string(s):
    indexStart = 0
    indexEnd = len(s) - 1
    while indexStart < indexEnd:
        s[indexStart],s[indexEnd] = s[indexEnd],s[indexStart]
        indexStart += 1
        indexEnd -= 1
    return s

input_array1 = ["h","e","l","l","o"]
input_array2 = ["H","a","n","n","a","h"]

Output1 = Reverse_string(input_array1)
Output2 = Reverse_string(input_array2)

print(Output1)
print(Output2)

