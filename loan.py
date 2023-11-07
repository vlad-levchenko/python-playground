
# Get details of loan
money_owed = float(input('How much money you owe, in dollars?\n'))              # 50,000
apr = float(input('What is the annual percentage rate (APR) of the loan?\n'))   # 3%
payment = float(input('How much will you pay off each month in dollars?\n'))    # $1,000
months = int(input('How many months do you want to see the results for?\n'))    # 24 months

monthly_rate = apr / 100 / 12

for x in range(months):

    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    #add in interest
    money_owed = money_owed + interest_paid
    
    if(money_owed - payment < 0):
        print('The last payment', money_owed)
        print('You paid off the loan in', x + 1, 'months')
        break

    # Make a payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest.', end = ' ')
    print('Now I owe', money_owed)


