
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position: ', self.position)

    def eat(self):
        print('I am hungry')


class RobotDog(Robot):
    def makeNoise(self):
        print('Woof Woof!')

    def eat(self):
        super().eat()
        print('I like bacon!')


# Main Program
def main():
    myRobotDog = RobotDog('Moe')
    myRobotDog.walk(10)
    myRobotDog.makeNoise()
    myRobotDog.eat()
    
    
main()

