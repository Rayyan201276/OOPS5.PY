from abc import ABC, abstractmethod

class GameCharacter(ABC):
    """Abstract blueprint for all game characters. """

    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod #decorator: It is kind of a loud declaration for the subclass inherited from it.
    def attack(self, target):
        pass

       
    @abstractmethod
    def take_damage(self, amount):
        pass

    @abstractmethod
    def is_alive(self):
        return self.health > 0


class Warrior(GameCharacter):
    def attack(self, target):
        damage = 25
        print(f"{self.name} swings a sword at {target.name} for {damage} damage!" )

    def take_damage(self, amount):
        actual_damage = max(1, amount - 5)  # armor
        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage (armor reduced). Health: {self.health} ")


class Mage(GameCharacter):
    def attack(self, target):
        damage = 40
        print(f"{self.name} casts a fireball at {target.name} for {damage} damage!")

    def take_damage(self, amount):
        actual = max(1, amount - 5)  # Magic shield
        self.health -= actual
        print(f"{self.name} takes {actual} damage (shield blocked). Health: {self.health} ")

def battle(character1, character2):
    print(f"Battle starts: {character1.name} vs {character2}!\n")
    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        if character2.is_alive():
            character2.attack(character1)
        print("---")
    winner = character1 if character1.is_alive() else character2
    print(f"{winner.name} wins!")

grom = Warrior("Grom" , 120)
jaina = Mage("Jaina", 80)
battle (grom, jaina)
