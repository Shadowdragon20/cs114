
Character={}


def intro():
    print('SPACE DUNGEON')
    print('what is your name?')
    player=input()

    # Character='player'

    return player

def get_char_class():

    print("choose a class?(Knight=1, Gunner=2, Mage=3)")
    charclass_lst=['Knight(1)', 'Gunner(2)', 'Mage(3)']
    char_class=int(input())

    if char_class ==1:
        print('Knight')
    # elif char_class==2:
    #     print('Mage')
    # elif char_class ==3:
    #     print('Gunner')
    return char_class



    # while (!=)

# def stats():
#     print('Costumize your stats( hit points and magic points has to equal 100)')
#     hit_points=input('hit points')
#     magic_points=input('magic points')
#     return stats

def main():
    player= intro()
    get_char_class()=
    # attributes = stats(attributes)
    print('You are', player, 'and you are a', char_class, '.') #'you have, ', attributes, )
main()
