

def main():
    # x = int(input('What\'s x? '))
    # y = float(input('What\'s y? '))
    
    # print('x squared is', square(x))
    remainderDivision(10, 0)
    
def square(n):
    # return n ** 2
    return pow(n, 2)

# z = int(x) + int(y)

# z = round(x + y)
# z = round(x / y, 2)
# z = x / y

# print(f'{z:,}')
# print(f'{z:.2f}')

def remainderDivision(a, b):
    
    if b == 0:
        raise Exception('Cannot divide by zero')
    
    result = a // b
    reminder = a % b
    
    print(a, '/', b, 'is', result, 'reminder', reminder)


main()