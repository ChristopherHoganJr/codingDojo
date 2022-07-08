class Fighter:
    def __init__(self, name, age, weapon, ability, strength, weight, speed):
        print('running the fighter constructor')
        self.name = name
        self.age = age
        self.weapon = weapon
        self.ability = ability
        self.strength = strength
        self.weight = weight
        self.speed = speed
        self.percent = 0
        self.shielding = False

    def shield(self):
        self.shielding = True
        print(f'{self.name} has put up their shield')

    def print_status(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'weapon: {self.weapon}')
        print(f'ability: {self.ability}')
        print(f'strength: {self.strength}')
        print(f'weight: {self.weight}')
        print(f'speed {self.speed}')
        print(f'percent: {self.percent}')
    
    def attack(self, opponent):
        if opponent.shielding == True:
            print(f'{self.name} attacked {opponent.name} but the shield blocked it!')
            opponent.shielding = False
        else:
            damage = 6
            opponent.percent += damage
            print(f'{self.name} attacked {opponent.name} and dealt {damage}%!!!')

    def special(self, opponent):
        if opponent.shielding == True:
            print(f'{self.name} special attacked {opponent.name} but the shield blocked it!')
            opponent.shielding = False
        else:
            damage = 15
            opponent.percent += damage
            print(f'{self.name} did a special attack!!!!')


# samus = Fighter('Samus', 29, 'arm cannon', 'ranged weapons', 8, 8, 4)
link = Fighter('Link',17,'sword','adventurer tools', 6, 6, 6)
# # print(samus.name)
# # print(link.name, link.ability, link.percent)
# samus.shield()
# link.special(samus)
# link.attack(samus)

class Samus(Fighter):
    def __init__(self):
        print('calling the samus constructor!')
        super().__init__('Samus',29,'arm cannon', 'curl up in a ball', 8, 8, 4)
        self.charged = False
    def special(self, opponent):
        if(self.charged):
            if opponent.shielding == True:
                print(f'{self.name} special attacked {opponent.name} but the shield blocked it!')
                opponent.shielding = False
            else:
                damage = 32
                opponent.percent += damage
                print(f'{self.name} fired her lazer and did {damage}')
        else:
            self.charged = True
            print(f'{self.name} is charing her arm cannon!')

samus = Samus()
samus.special(link)
link.shield()
samus.special(link)
