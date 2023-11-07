from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, newEmployee):
        self.employees.append(newEmployee)

    def displayEmployees(self):
        print('Current Employees:')
        
        for x in self.employees:
            print(x.firstName, x.lastName)
        print('------------------------')

    def payEmployee(self):
        print('Paying Employees:')
        for x in self.employees:
            print('Paycheck for:', x.firstName, x.lastName)
            print(f'Acount: ${x.calculatePaycheck():,.2f}')
        print('------------------------')



def main():
    myCompany = Company()
    
    employee1 = Employee('Sarah', 'Hess', 50000)
    myCompany.addEmployee(employee1)
    
    employee1 = Employee('Lee', 'Smith', 25000)
    myCompany.addEmployee(employee1)
    
    employee1 = Employee('Bob', 'Brown', 65000)
    myCompany.addEmployee(employee1)

    myCompany.displayEmployees()
    myCompany.payEmployee()

main()