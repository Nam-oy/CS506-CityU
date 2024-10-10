def Reduced_to_Zero(num):
    Output = 0
    while num > 0:
        if (num % 2) != 0:
            num = num - 1
            Output += 1
        else:
            num = num // 2
            Output += 1
    return Output


num = 14
step = Reduced_to_Zero(num)
print ("Output : ", step)


Num = int(input())
print("Input Num = 14" + str(Num))

Output = 0
while Num > 0:
    if (Num % 2) != 0:
        Num = Num - 1
        Output += 1
    else: 
        Num = Num // 2
        Output += 1

print("Output : " + str(Output))


