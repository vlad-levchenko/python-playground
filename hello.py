# Ask user for their name
# Remove whitespace and Capitalize  str
# name = input('What\'s your name? ').strip().title()

# split user's name into first name and last name
# first, last = name.split(' ')

# Say hello to user
# print(f'hello, {first}')


def main():
    hello()

    name = input('What\'s your name? ')

    hello(name) 

def hello(to = 'world'):
    print(f'Hello, {to}')



main()

