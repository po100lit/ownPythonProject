# Крестики-Нолики
import os

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_size = 3


def draw_board():
    print('-' * (4 * board_size - 1))
    for i in range(board_size):
        print(f' {board[i * board_size]} | {board[1 + i * board_size]} | {board[2 + i * board_size]} ')
        print('-' * (4 * board_size - 1))


def game_step(index, char):
    if 1 > index > 9 or board[index - 1] in ('X', 'O'):
        return False
    else:
        board[index - 1] = char
        return True


def check_win():
    win = False
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for pos in win_combinations:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win


def start_game():
    current_player = 'X'
    step = 1

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board()

    while step < 10 and not check_win():
        index = input(f'{current_player}, take your move, or 0 to exit...: ')
        if index == '0':
            break
        if game_step(int(index), current_player):
            print('Good move')
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            os.system('cls' if os.name == 'nt' else 'clear')
            draw_board()

            step += 1
        else:
            print('Bad move')
    print(f'{check_win()} is winner!!!' if check_win() != False else f'{current_player} has technical win')


if __name__ == "__main__":
    print('Welcome to TIC-TAC-TOE')
    start_game()
