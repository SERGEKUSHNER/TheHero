from hero import Hero
from villains import Villain


class Battle:

    def __init__(self):
        self.hero = Hero()
        self.villain = Villain()

    def battle(self):

        self.battle_beginner()

        for x in range(21):
            if self.hero.health <= 0 or self.villain.health <= 0:
                print('Game Completed')
                self.winner()
                break
            else:
                if x == 20:
                    self.winner()
                else:
                    if Hero.attacker:
                        print('Battle number ', x)
                        self.hero.attack(self.villain)
                    else:
                        print('Battle number ', x)
                        self.villain.attack(self.hero)

    def battle_beginner(self):
        if self.hero.speed > self.villain.speed:
            print("hero.speed is: %s, hero.health is: %s , villain.speed is %s, villain.health is %s" % (
            self.hero.speed, self.hero.health, self.villain.speed, self.villain.health))
            Hero.attacker = True

        if self.hero.speed < self.villain.speed:
            print("hero.speed is: %s, hero.health is: %s , villain.speed is %s, villain.health is %s" % (
            self.hero.speed, self.hero.health, self.villain.speed, self.villain.health))
            Hero.attacker = False

        if self.hero.speed == self.villain.speed:
            print("hero.speed is: %s, hero.health is: %s , villain.speed is %s, villain.health is %s" % (
            self.hero.speed, self.hero.health, self.villain.speed, self.villain.health))
            if self.hero.luck > self.villain.luck:
                print("hero.luck is: %s, hero.health is: %s ,villain.luck is: %s, villain.health is: %s" % (
                self.hero.luck, self.hero.health, self.villain.luck, self.villain.health))
                Hero.attacker = True
            else:
                print("hero.luck is: %s, hero.health is: %s ,villain.luck is: %s, villain.health is: %s" % (
                self.hero.luck, self.hero.health, self.villain.luck, self.villain.health))
                Hero.attacker = False

    def winner(self):
        if self.hero.health <= 0 and self.villain.health > 0:
            print("vilain is the winner, where villain.health is %s, and hero.health is %s" % (
                self.villain.health, self.hero.health))
        if self.hero.health > 0 and self.villain.health <= 0:
            print("hero is the winner, where hero.health is %s, and villain.health is %s" % (
                self.hero.health, self.villain.health))


A = Battle()
A.battle()
