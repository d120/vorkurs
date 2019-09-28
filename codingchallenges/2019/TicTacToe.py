import random
import sys

# The game board is a list with the numbers 1 to 9
board = [i for i in range(0, 9)]

# The player figures
player = 'X'
computer = 'O'

# winning move combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def print_board():
    x = 1
    line = '-------------\n'
    line += '| '
    for i in board:
        line += str(i)
        line += ' | '
        if x % 3 == 0:
            line += '\n'
            line += '-------------'
            print(line)
            line = '| '
        x += 1


def can_move(move):
    if board[move] == move:
        return True
    return False


def has_won(player):
    for tup in winners:
        win = True
        for ix in tup:
           if board[ix] != player:
               win = False
        if win:
            return win
    return win

def make_move(player, move):
    if can_move(move):
        board[move] = player

def test_move(player, move):
    if can_move(move):
        board[move] = player
        win = has_won(player)
        board[move] = move
        return win

def computer_move():
    # If I can win, others don't matter.
    for i in range(0, 9):
        if test_move(computer, i):
            return make_move(computer, i)
    # If player can win, block him.
    for i in range(0, 9):
        if test_move(player, i):
            return make_move(computer, i)
    # Otherwise, try to take one of desired places.
    possible_moves = []
    for i, x in enumerate(board):
        if x != player and x != computer:
            possible_moves.append(i)
    return make_move(computer, random.choice(possible_moves))

def game_over():
    if board.count(player)+board.count(computer) == 9:
        return True
    return False

print('Player Figure/Symbol/Character:')
player = input()
print('Computer Figure/Symbol/Character:')
computer = input()
print('Player is [%s] and computer is [%s]' % (player, computer))
result = '%%% Deuce ! %%%'

current_player = computer

while not game_over():
    print_board()

    if has_won(current_player):
        print(current_player, 'won !')
        sys.exit()

    if current_player == player:
        current_player = computer
    else:
        current_player = player

    if player == current_player:
        print('# Make your move ! [0-8] : ', end='')
        move = int(input())
        if can_move(move):
            make_move(current_player, move)
        else:
            print('Invalid number ! Try again !')
            current_player = computer
        continue

    if current_player == computer:
        computer_move()
        continue


print_board()
print("Unentschieden")




