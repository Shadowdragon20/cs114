print('****SPACE DUNGEON****')

print('Character Name?')
# name=input()
#
# print('What class would you like to play as (Mage, Knight, or Gunner?)')
# job=input()
#
# print('****Stat Customization****:')
# print('How much points do you want to add on to attack and magic?, (must add to 100)')
# print('attack stat:')
# num1=input()
# print('magic stat:')
# num2=input()
#
# print('You begin your adventure as an adventurer named ' + name +' as a ' + job + '.' #' You have ' + num1 + ' attack and '+ num2 + ' magic attack.')


def new_game():
    player=input()
    return player

print("choose a class?(Knight=1, Gunner=2, Mage=3)")

def get_job():
    job_list=['Knight(1)', 'Gunner(2)', 'Mage(3)']
    job=input()

    if job == 1:
        print (job_list=[0])
    # elif == 2:
    #     print('Gunner')
    #   elif == 3:
    #     print('Mage')
    return job

player = {
'HP': 100,
'attack': 100,
'defense': 100,
'PP':100,
'name': name
}
def Power_Points(player):







def main():
    player = new_game()
    job = get_job()
    print('You are', player, 'and you are a', job, '.' )

main()
