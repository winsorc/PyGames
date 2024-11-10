import random

def roll_dice(amount: int = 2, sides: int = 6):
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] =[]
    for i in range(amount):
        random_roll: int = random.randint(1,sides)
        rolls.append(random_roll)

    return rolls

def roll_total(rolls):
    total = 0
    for i in rolls:
        total += i
    return total

def main():
    while True:
        try:
            print('---------------------------------------------------')
            print(f'             Dungeon Dice Roller 1.0')
            print('---------------------------------------------------')
            print(f'Select number of sides and number of dice to roll.')
            print(f'Type exit to quit')
            print('----------------------------------------------------')
            num_sides: str = input('How many sides on your dice? ')
            num_dice: str = input('How many dice to roll? ')

            if num_dice.lower() == 'exit' or num_sides == 'exit':
                print('Thanks for playing!')
                break

            rolls = roll_dice(int(num_dice), (int(num_sides)))
            total = roll_total(rolls)
            print(*rolls)
            print(f'Total: {total}')
        except ValueError:
            print('(Please enter a valid number)', sep =', ')

if __name__ == '__main__':
    main()

#add total of all rolls function
#add other sided dice
