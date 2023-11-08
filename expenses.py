# python expenses.py

expenses = [10.50, 8, 5, 15, 20, 5, 3]


total = sum(expenses)
sum1 = 0

for x in expenses:
    sum1 = sum1 + x

print('Using sum() - You spent $', sum1, sep = '')
print('You spent $', sum1, sep = '')


total1 = 0
expenses1 = []
for x in range(0, 7, 1):
    expenses1.append(float(input('Enter an expense:')))
    print(expenses1)

total1 = sum(expenses1)

print('You spent $', total1, sep = '')

