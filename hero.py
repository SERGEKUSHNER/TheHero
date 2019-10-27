import random



class Hero:
    attacker = False

    def __init__(self):
        print('Hero constructor initlialized')
        self.health = random.randrange(70, 100)
        self.strength = random.randrange(70, 80)
        self.defence = random.randrange(45, 55)
        self.speed = random.randrange(40, 55)
        self.luck = (random.randrange(10, 30))/100
        self.criticStrike = 0.1
        self.extraCriticStrike = 0.01
        self.resilience = 0.2
        # self.luck = Hero.initialLuck
        # print('Hero initial Luck is', Hero.initialLuck)

    def criticallStrike(self, villain):
        print('This is criticallStrike check')
        randomNumber = random.random()
        print('randomNumber < self.criticStrike', randomNumber < self.criticStrike)
        print('randomNumber < self.extraCriticStrike', randomNumber < self.extraCriticStrike)
        if (randomNumber < self.criticStrike) and (randomNumber < self.extraCriticStrike):
            print("extra critical strike is in action")
            damage = self.strength - villain.defence
            villain.health = villain.health - damage
            print("hero.health is %d, and villain.health is %d and damage done is %d" % (self.health, villain.health, damage))
        return randomNumber < self.criticStrike

    def attack(self, villain):
        if villain.counterResilience == 1:
            print('next time Hero will not have Resilience')
            villain.flag = False
            villain.counterResilience = 0
        print('Hero attacks!')
        villainGotLucky = self.villainGotLucky(villain)
        if villainGotLucky:
            print('Villain got lucky, will not get any damage')
            print("hero.health is %d, and villain.health is %d" % (self.health, villain.health))
        else:
            damage = self.strength - villain.defence
            villain.health = villain.health - damage
            print("hero.health is %d, and villain.health is %d and damage done is %d " %(self.health, villain.health, damage))
        if villainGotLucky:
            print('No Critical Strike Ckeck')
        else:
            if self.criticallStrike(villain):
                print('Critical Strike is in action')
                damage = self.strength - villain.defence
                villain.health = villain.health - damage
                print("hero.health is %d, and villain.health is %d and damage done is %d" % (self.health, villain.health, damage))

        Hero.attacker = False

    def villainGotLucky(self, villain):
        randomNumber = random.random()
        print("probRange is %s and randomNumber is %s" % (villain.luck, randomNumber))
        print('Villain is lucky ?', randomNumber < villain.luck)
        return randomNumber < villain.luck
