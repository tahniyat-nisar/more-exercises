
def win():
    print ('You win!')

def lose():
    print ('You lose!')

def once_agian():
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    from random import randint
    moves = ['rock', 'paper', 'scissors']
    random_move = randint(0, 2)

    computer_choice =moves[random_move]

    if player_choice ==computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'paper':
        win()
    elif player_choice == 'paper' and computer_choice == 'scissors':
        win()
    elif player_choice  == 'scissors' and computer_choice == 'rock':
        win()
    else: 
        lose()

(once_agian())        
again = input('Do you want to play again? (y or n)').strip()
if again == 'n':
    print("OK")
else:
    i=1
    while i>=0:
        once_agian()

# Rock Paper se haar jata hai

# Paper Scissors se haar jaata hai

# Aur, Scissors Rock se.

