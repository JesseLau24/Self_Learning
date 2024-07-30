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
    def touchdown(self):
        self.points += 7
        self.party()
        print(f'{self.name} points {self.points}')

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()



