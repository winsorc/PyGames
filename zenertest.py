from random import randint

guess_count = 25
num_correct = 0



while guess_count > 0:
    print(f'Guess the symbol that will appear.')
    print(f'○, +, §, ♦, *')
    print(f'1 = ○, 2 = +, 3 = §, 4 = ♦, 5 = *')
    print()
    lower_num, higher_num = 1, 5
    random_number: int = randint(lower_num, higher_num)
    5

    if random_number == 1:
        symbol = '○'
    elif random_number == 2:
        symbol = '+'
    elif random_number == 3:
        symbol = '§'
    elif random_number == 4:
        symbol = '♦'
    elif random_number == 5:
        symbol = '*'

    try:
        print()
        user_guess = int(input(f'Enter number 1-5 to select symbol:'))
        print()
        if user_guess > 5:
            raise Exception('Incorrect value. Enter a number 1 - 5')
    except ValueError:
        print('Incorrect value. Enter a number 1 - 5')
    
    print(f'Symbol is {symbol}')
    if user_guess == random_number:
            print('You were correct!')
            print()
            num_correct += 1
    else: 
        print('Sorry, that was incorrect')
        print()
    guess_count -= 1
    print(f'{guess_count} attempts left')


print(f'You had {num_correct} correct guesses')
print()
if num_correct < 3:
    print(f'Yikes. That is unusually poor performance!')
if num_correct >= 3 and num_correct <= 7:
    print(f'Expected range based on chance. 79% of people fall within this range.')
if num_correct >= 8 and num_correct <= 14:
    print(f'Within realm of chance. Out of a group of 25 people, 10.9% will score in this range.')
if num_correct >=15 and num_correct >= 19:
    print(f'Chance of this score is 1 in 90,000. Maybe a little psychic? Or just lucky?')
if num_correct >= 20 and num_correct <=24:
    print(f'If you are not cheating, go play the lottery and trust your intuition. There is only a 1 in 5 Billion chance of this score ocurring.')
if num_correct == 25:
    print(f'No way! You have ESP. There is only a 1 in 300 quadrillion chance of getting this score. Call the Randi Foundation NOW!!')

    



