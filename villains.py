from hero import Hero
import random


class Villain:

    def __init__(self):
        print('Villain constructor initlialized')
        self.health = random.randrange(60, 90)
        self.strength = random.randrange(60, 90)
        self.defence = random.randrange(40, 60)
        self.speed = random.randrange(40, 60)
        self.luck = (random.randrange(25, 45)) / 100
        self.counterResilience = 0
        self.flag = True

    def attack(self, hero):
        print('Villain attacks')
        if self.heroGotLucky(hero):
            print('Hero got lucky, will not get any damage')
            print("hero.health is %d, and villain.health is %d" % (hero.health, self.health))
        else:
            if self.flag:
                if self.gotResilience(hero):
                    print('Resilience is in action')
                    damage = (self.strength - hero.defence) / 2
                    hero.health = hero.health - damage
                    print("hero.health is %d, and villain.health is %d and damage done is %d" % (hero.health, self.health, damage))
                    self.counterResilience = self.counterResilience + 1
                else:
                    damage = self.strength - hero.defence
                    hero.health = hero.health - damage
                    print("hero.health is %d, and villain.health is %d and damage done is %d" % (hero.health, self.health, damage))

            else:
                damage = self.strength - hero.defence
                hero.health = hero.health - damage
                print("hero.health is %d, and villain.health is %d and damage done is %d" % (hero.health, self.health, damage))
                self.flag = True
        Hero.attacker = True

    def heroGotLucky(self, hero):
        randomNumber = random.random()
        print("hero.luck is %s and randomNumber is %s" % (hero.luck, randomNumber))
        print('Hero is lucky ?', randomNumber < hero.luck)
        return randomNumber < hero.luck

    def gotResilience(self, hero):
        print('Resilience is checked')
        randomNumber = random.random()
        print("hero.resilience is %s and randomNumber is %s" % (hero.resilience, randomNumber))
        print("randomNumber < hero.resilience is %s" % (randomNumber < hero.resilience))
        return randomNumber < hero.resilience
