#Ask for the amount of change to dispense in cents. Assume that the amount input will be less than 100 cents.

#Calculate the number of quarters necessary first.

#Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins.

print('How much change would you like in cents?')

change=int(input())

num_quarters = change // 25

change = change - (num_quarters * 25)

num_dimes = change // 10

change = change - (num_dimes * 10)

num_nickels= change // 5

change = change - (num_nickels * 5)

num_pennies = change // 1
change= change - (num_pennies * 1)

print("your new amount is " + str(num_quarters) + " quarters " + str(num_dimes) + " dimes " + str(num_nickels) + " nickels " + str(num_pennies) + " pennies")
