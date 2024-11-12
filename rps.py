import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')

        self.moves: dict = {'rock': '🧱', 'paper': '🧻', 'scissors': '✂'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score = 0
        self.ai_score = 0

    def play_game(self):
        user_move: str = input('Rock, paper or scissors? >> ').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            print(f'AI Score: {self.ai_score}  User Score: {self.user_score}')
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
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!') 
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
        else:
            print('AI Wins.')

    def add_score(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            pass
        elif user_move == 'rock' and ai_move == 'scissors':
            self.user_score +=1
        elif user_move == 'paper' and ai_move == 'rock':
            self.user_score +=1
        elif user_move == 'scissors' and ai_move == 'paper':
            self.user_score +=1
        else:
            self.ai_score += 1
        
        
if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()


        
        ##add score system