import random
import sys

"""text based game where user makes decisions which affect a series of
encounters with 'enemies'"""
print('****SPACE DUNGEON****')

print('Character Name?')
name=input()

print('what is the name fo your ship?')
ship=input()

# print('What class would you like to play as (Mage, Knight, or Gunner?)')
# job=input()
# print('You begin your adventure as an adventurer named ' + name +' as a ' + job + '.' #' You have ' + num1 + ' attack and '+ num2 + ' magic attack.')

print('The player enters the hallway to the cargo bay. It was dim, sparks coming from broken light fixtures, and some floor panels looked like something had pried them open. You slowly and quitely make your way through the hallway.')
input('Press any key to continue')
player = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': name
}

enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
'name': 'Zombie AI human'
}

enemy2 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Zombie crewman'
}

enemy3 = {
'HP': 50,
'attack': 50,
'defense': 50,
'name': 'Pack of zombie mutated dogs'
}





def game_over(player):
    print("GAME OVER -- ", player['name'], ',You and everyone on', ship , 'are dead, dessicated carbon. Decades\
     from now a scientific survey vessel will stumble across your ship and investigators\
     will log the incident.')
    return sys.exit()


def get_item(player):
    item_list = ["MRE", "First Aid Kit", "Meth-derived stim-pack"]

    print("You find a ", item_list[random.randint(0, 2)], "your health increased by ",
    (abs(player['HP'] - 100)), "HP")
    player['HP'] += (abs(player['HP'] - 100))
    return player


def attack(opponent):
    rand_damage = random.randint(8, 32)
    opponent['HP'] -= rand_damage
    print(rand_damage, " damage!")
    return opponent


def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print(name ,'oppo1 HP: ', oppo1['HP'])
    print('enemy1  oppo2 HP: ', oppo2['HP'])


def encounter(player, opponent):
    if player['HP'] > 70:
        fight(player, opponent)
        # if player['HP'] <= 0:
        #     return game_over(player)
        input('Press any key to continue')
    elif opponent['name'] == 'Zombie AI human':
        fight(player, opponent)
        # return player
    else:
        get_item(player)
        input('Press any key to continue')


"""there are 4 encounters, each encounter offers an option to open a door,
the door will either have an enemy or an item"""


def main():
    # fight(player, enemy1)

    # get_item(player)

    print('A pack of zombie mutated dogs make there way out of the broken floor panels ...\n\n')
    encounter(player, enemy3)
    print('you start running through the hallway and stumble across...\n\n')
    encounter(player, enemy2)
    print('encounter 3...\n\n')
    encounter(player, enemy1)
    print("YOU HAVE ESCAPED ", name , " HP: ", player['HP'])


if __name__ == "__main__":
    # print("Executing as main program")
    # print("Value of __name__ is: ", __name__)
    main()
