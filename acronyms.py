

def findAcronym():
    lookup = input('What software acronym would you like to look up?\n')

    found = False
    try:
        with open('./files/acronyms.txt') as file:
            for line in file:
                if lookup in line:
                    print(line)
                    found = True
                    break
    except:
        print('File does not exist')
        return
                
    
    if not found:
        print('The acronym not found', lookup)
                   

def addAcronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?\n')

    with open('./files/acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')



def main():
    # ask the user whether they want to find or ro add an acronym
    choice = input('Do you want to find (F) or add (A) an acronym?\n')
    
    if choice == 'F':
        findAcronym()
    elif choice == 'A':
        addAcronym()

main()
    