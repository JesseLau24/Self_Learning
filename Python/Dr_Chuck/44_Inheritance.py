class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam

    def party(self):
        self.x += 1
        print(f'{self.name} party count {self.x}')

class FootballFan(PartyAnimal):
    points = 0
    def __init__(self, nam):
        super().__init__(nam)  
        # Call the __init__ method of the parent class
        # could be ommited, but it's better to keep it

    def touchdown(self):
        self.points += 7
        self.party()
        print(f'{self.name} points {self.points}')

s = PartyAnimal('Sally')
s.party()
# for Sally, the party count would be updated and stored each 
# time .party() is called
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown() 
# for Jim,too, the touchdown points and party counts would be 
# updated and stored in memory
j.touchdown()



