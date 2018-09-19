#Opening exercise:

#Write a program that takes in input from a user and returns a response based on the length of string the user inputs.
import random
num = random.randint(1,6)

print('type something random.')
type=len(input())


if num == 1:
    print('wow')
elif num == 2:
    print('alright i see')
elif num == 3:
    print(':p')
elif num == 4:
    print('luck you')
elif num == 5:
    print('just five more')
elif num > 6:
    print('I dont know how to compute this...')
