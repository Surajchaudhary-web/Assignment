# create a class named Animal
# define different attributes like (leg, eye, ear, tail, ...)
# define method to get the data and a method to print out the animal detail
# create classes Dog and cat that inherits Animal class. define a method named sound, and override the detail method

class Animal:
    def __init__(self, name, leg, eye,ear,tail, horn):
        self.name = name
        self.leg = leg
        self.eye = eye
        self.ear = ear
        self.tail =  tail
        self.horn = horn
    def sound(self):
        print("sound = sound of the animal")

    def show_detail(self):
        print(f"""Name = {self.name}
Leg = {self.leg}
Eye = {self.eye}
Ear = {self.ear}
Tail = {self.tail}
Horn = {self.horn}""")

class Dog(Animal):
    voice =  None
    def sound(self,voice = "Bark" ):
        self.voice = voice
    def show_detail(self):
        print(f"voice = {self.voice}")
class Cat(Animal):
    voice = None
    def sound(self,voice = "Mew"):
        self.voice = voice
    def show_detail(self):
        print(f"voice = {self.voice}")
d1 = Dog("dog",4,2,2,1,0)
d1.sound()
d1.show_detail()
d1 = Cat("cat",4,2,2,1,0)
d1.sound()
d1.show_detail()

