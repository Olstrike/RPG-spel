class character:

    def __init__(self, name, health, attack, armor) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
    
    def __str__(self) -> str:
        return f"name: {self.name}\n {self.health}\n {self.attack}\n {self.armor}"