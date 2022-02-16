import recources
from recources import Character, Goblin
from random import randint, shuffle, choice

def fight(players  : list, enemies : list):

    partisipants = players + enemies #
    shuffle(partisipants)

    for char in partisipants:
        target = ""
        # Is it a player or an npc
        if char in players: 
            target = choice(enemies)
        else:
            target = choice(players)

        target.take_damage(char.get_attack())

        if target.get_health() == 0:
            print(f"{target.get_name()} has died")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            partisipants.remove(target)

        else:
            print(f"{target.get_name()} has {target.get_health()} hp remaining.")

        if len(enemies) == 0 or len(players) == 0:
            break




if __name__ == "__main__":
    enemies = []
    players = []
    emy = Character("Emy", 20, 5, 2)
    nick = Character("Nick", 15, 2, 1)
    players.append(emy)
    players.append(nick)

    enemies.append(Goblin(10, 3, 2, 1))
    enemies.append(Goblin(15, 2, 1, 2))
    enemies.append(Goblin(12, 3, 1, 3))

    round = 1
    while len(enemies) != 0 and len(players) != 0:
        print(f"ROUND {round}, FIGHT!")
        fight(players, enemies)
        print()
        round +=1 

    if len(enemies) == 0:
        print("The players won FATALITY!!!!")
    elif len(players) == 0:
        print("The goblins win, u loose")


