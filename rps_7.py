import random
import sys
## 7 move version of Rock Paper Scissors
## Based on rps7 from umop.com
class RPS:
    def __init__(self):
        print('-------------------')
        print('Welcome to RPS 7!')
        print('------------------')
        print('There are 7 gestures to choose from.')
        print('-------------------------------------------------------------------')
        print('ROCK 🧱 POUNDS OUT FIRE 🔥, CRUSHES SCISSORS ✂  & SPONGE 🧽.')
        print('FIRE 🔥 MELTS SCISSORS ✂, BURNS PAPER 🧻 & SPONGE 🧽.')
        print('SCISSORS ✂ SWISH THROUGH AIR 💨, CUT PAPER 🧻  & SPONGE 🧽.')
        print('SPONGE 🧽 SOAKS PAPER 🧻, USES AIR 💨 POCKETS, ABSORBS WATER 💧.')
        print('PAPER 🧻 FANS AIR 💨, COVERS ROCK 🧱, FLOATS ON WATER 💧.')
        print('AIR 💨 BLOWS OUT FIRE 🔥, ERODES ROCK 🧱, EVAPORATES WATER 💧.')
        print('WATER 💧 ERODES ROCK 🧱, PUTS OUT FIRE 🔥, RUSTS SCISSORS ✂.')
        print('--------------------------------------------------------------------')
        print() #blank line

        self.moves: dict = {'rock': '🧱', 'paper': '🧻', 'scissors': '✂', 'fire': '🔥', 'water': '💧', 'air': '💨', 'sponge': '🧽'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        user_move: str = input('Rock, paper, scissors, fire, water, air, or sponge? >> ').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            print() #blank line
            print(f'AI Score: {self.ai_score}  User Score: {self.user_score}')
            print() #blank line
            print('Programmed by WinsC1 11/24. Game rules by umop.com.')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        self.add_score(user_move, ai_move)
        
        



    def display_moves(self, user_move: str, ai_move: str):
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a tie!')
            #rock moves
        elif user_move == 'rock' and ai_move == 'scissors':
            print('Rock Crushes Scissors!')
            print('You win!')
        elif user_move == 'rock' and ai_move == 'fire':
            print('Rock Pounds out Fire!')
            print('You win!')
        elif user_move == 'rock' and ai_move == 'sponge':
            print('Rock Crushes Sponge!')
            print('You win!')
            #fire moves
        elif user_move == 'fire' and ai_move == 'scissors':
            print('Fire Melts Scissors!')
            print('You win!')
        elif user_move == 'fire' and ai_move == 'paper':
            print('Fire Burns Paper!')
            print('You win!')
        elif user_move == 'fire' and ai_move == 'sponge':
            print('Fire Burns Sponge!')
            print('You win!')
            #paper moves
        elif user_move == 'paper' and ai_move == 'rock':
            print('Paper Covers Rock!')
            print('You win!')
        elif user_move == 'paper' and ai_move == 'air':
            print('Paper Fans Air!')
            print('You win!')
        elif user_move == 'paper' and ai_move == 'water':
            print('Paper Floats on Water!')
            print('You win!')
            #scissors moves 
        elif user_move == 'scissors' and ai_move == 'paper':
            print('Scissors Cut Paper!')
            print('You win!')
        elif user_move == 'scissors' and ai_move == 'air':
            print('Scissors Swishes through Air!')
            print('You win!')
        elif user_move == 'scissors' and ai_move == 'sponge':
            print('Scissors Cut Sponge')
            print('You Win!')
            #sponge moves
        elif user_move == 'sponge' and ai_move == 'paper':
            print('Sponge Soaks Paper!')
            print('You Win!')
        elif user_move == 'sponge' and ai_move == 'air':
            print('Sponge Uses Air Pockets!')
            print('You Win!')
        elif user_move == 'sponge' and ai_move == 'water':
            print('Sponge Absorbs Water!')
            print('You Win!')
            #air moves
        elif user_move == 'air' and ai_move == 'fire':
            print('Air Blows Out Fire!')
            print('You Win!')
        elif user_move == 'air' and ai_move == 'rock':
            print('Air Erodes Rock!')
            print('You Win!')
        elif user_move == 'air' and ai_move == 'water':
            print('Air Evaporates Water!')
            print('You Win!')
            #water moves
        elif user_move == 'water' and ai_move == 'rock':
            print('Water Erodes Rock!')
            print('You Win!')
        elif user_move == 'water' and ai_move == 'fire':
            print('Water Puts Out Fire!')
            print('You Win!')
        elif user_move == 'water' and ai_move == 'scissors':
            print('Water Rusts Scissors!')
            print('You Win!')
        else:
            print('AI Wins.')

    def add_score(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            pass
            #rock score
        elif user_move == 'rock' and ai_move == 'scissors':
            self.user_score +=1
        elif user_move == 'rock' and ai_move == 'fire':
            self.user_score +=1
        elif user_move == 'rock' and ai_move == 'sponge':
            self.user_score +=1
            #fire score
        elif user_move == 'fire' and ai_move == 'scissors':
            self.user_score +=1
        elif user_move == 'fire' and ai_move == 'paper':
            self.user_score +=1
        elif user_move == 'fire' and ai_move == 'sponge':
            self.user_score +=1
            #paper score
        elif user_move == 'paper' and ai_move == 'rock':
            self.user_score +=1
        elif user_move == 'paper' and ai_move == 'air':
            self.user_score +=1
        elif user_move == 'paper' and ai_move == 'water':
            self.user_score +=1
            #scissors score
        elif user_move == 'scissors' and ai_move == 'paper':
            self.user_score +=1
        elif user_move == 'scissors' and ai_move == 'air':
            self.user_score +=1
        elif user_move == 'scissors' and ai_move == 'sponge':
            self.user_score +=1
            #sponge score
        elif user_move == 'sponge' and ai_move == 'paper':
            self.user_score +=1
        elif user_move == 'sponge' and ai_move == 'air':
            self.user_score +=1
        elif user_move == 'sponge' and ai_move == 'water':
            self.user_score +=1
            #air score
        elif user_move == 'air' and ai_move == 'fire':
            self.user_score +=1
        elif user_move == 'air' and ai_move == 'rock':
            self.user_score +=1
        elif user_move == 'air' and ai_move == 'water':
            self.user_score +=1
            #water score
        elif user_move == 'water' and ai_move == 'rock':
            self.user_score +=1
        elif user_move == 'water' and ai_move == 'fire':
            self.user_score +=1
        elif user_move == 'water' and ai_move == 'scissors':
            self.user_score +=1
        else:
            self.ai_score += 1
        
        
if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()


        
