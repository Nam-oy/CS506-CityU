def Add_Digits(num):
    while num >= 9:
        sum_num = 0
        while (num > 0):
            sum_num += num % 10
            num //= 10 
        num = sum_num
    return num





num = 38
Output = Add_Digits(num)
print ("Input : ", num, "Output :", Output )



def addDigits(num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

Formula = addDigits(num)
print ("Formula : ",Formula )




# following formula:
# Digital Root=1+(num−1)%9


