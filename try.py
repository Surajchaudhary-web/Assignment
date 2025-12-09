class Animal:
    def __init__(self):
        self.name = None
        self.leg = None
        self.eye = None
        self.ear = None
        self.tail = None

    # method to get user input
    def get_data(self):
        self.name = input("Enter animal name: ")
        self.leg = input("Enter number of legs: ")
        self.eye = input("Enter number of eyes: ")
        self.ear = input("Enter number of ears: ")
        self.tail = input("Enter number of tails: ")

    # method to print details
    def detail(self):
        print("\n--- Animal Detail ---")
        print(f"Name: {self.name}")
        print(f"Legs: {self.leg}")
        print(f"Eyes: {self.eye}")
        print(f"Ears: {self.ear}")
        print(f"Tails: {self.tail}")


# Child class Dog inheriting Animal
class Dog(Animal):
    def sound(self):
        print("Dog sound: Woof! Woof!")

    # overriding the detail method
    def detail(self):
        print("\n--- Dog Detail ---")
        super().detail()  # calling parent detail


# Child class Cat inheriting Animal
class Cat(Animal):
    def sound(self):
        print("Cat sound: Meow! Meow!")

    # overriding the detail method
    def detail(self):
        print("\n--- Cat Detail ---")
        super().detail()


# Example usage
dog = Dog()
dog.get_data()
dog.detail()
dog.sound()

cat = Cat()
cat.get_data()
cat.detail()
cat.sound()
