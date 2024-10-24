income = {'Alice' : 90000,'Bob' :100000,'Jeff':200000,'Apiwat':999998,'Stark':999999}

highest = max(income, key=income.get)
print("the richest man on earth:", end=' ')
print(highest + ' with $' + str(income[highest]))

lowest = min(income, key = income.get)
print("the lowest man on earth:", end=' ')
print(lowest + ' with $' + str(income[lowest]))
