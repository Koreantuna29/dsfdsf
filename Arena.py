from main.py import BattleBot

class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2
    def battle(self):
        while self.bbot1.is_alive() and self.bbot2.is_alive():
            #begin battle round
            if self.bbot1.speed <= self.bbot2.speed:
                self.bbot1.action(self.bbot2)
                self.bbot2.action(self.bbot1)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round")
            else:
                self.bbot2.action(self.bbot1)
                self.bbot1.action(self.bbot2)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round")
        if self.bbot1.is_alive():
            print(self.bbot1.name + " is the winner!")
        else:
            print(self.bbot2.name + " is the winner!")

Bot1 = 
Bot2 = 
Arena =  Arena(Bot1, Bot2)
arena.battle()