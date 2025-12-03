class Animal:
    name = None
    leg = None
    eye = None
    ear = None
    tail = None
    horn = None
    def get_data(self):
        self.name = input("Enter the name of animal:")
        self.leg = input("Enter the number of legs:")
        self.eye =  input("Enter the number of eyes:")
        self.ear =  input("Enter the number of ears:")
        self.tail =  input("Enter the number of tail:")
        self.horn =  input("Enter the number of horn:")
    
    def show_detail(self):
        print(f"""Name = {self.name}
Leg = {self.leg}
Eye = {self.eye}
Ear = {self.ear}
Tail = {self.tail}
Horn = {self.horn}""")


s1 = Animal()
s1.get_data()
s1.show_detail()
