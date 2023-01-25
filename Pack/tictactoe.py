class TicTacToeBoard:
    def __init__(self):
        self.first_player = 'X'
        # self.BLANCK = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        self._board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']

    def board_print(self):
        for i in range(9):
            print(self._board[i], sep='', end='  ')
            if i == 2 or i == 5:
                print()
        print()

    def board_check_not_finish(self) -> bool:
        return all(c == 'X' or c == 'O' for c in self._board)

    def step(self, target):
        if self.step_check(target):
            self._board[target - 1] = self.first_player
            self.player_change()
        else:
            print('Место занято - выбери другое!')
        self.board_print()

    def step_check(self, target) -> bool:
        if self._board[target - 1] not in ['X', 'O']:
            return True
        else:
            return False

    def win_check(self) -> bool:

        b = self._board
        if (b[0] == 'X' and b[1] == 'X' and b[2] == 'X' or
                b[3] == 'X' and b[4] == 'X' and b[5] == 'X' or
                b[6] == 'X' and b[7] == 'X' and b[8] == 'X' or
                b[0] == 'X' and b[4] == 'X' and b[8] == 'X' or
                b[2] == 'X' and b[4] == 'X' and b[6] == 'X'):
            print(f'\nWin {self.first_player} ')
            return True
        elif (b[0] == 'O' and b[1] == 'O' and b[2] == 'O' or
              b[3] == 'O' and b[4] == 'O' and b[5] == 'O' or
              b[6] == 'O' and b[7] == 'O' and b[8] == 'O' or
              b[0] == 'O' and b[4] == 'O' and b[8] == 'O' or
              b[2] == 'O' and b[4] == 'O' and b[6] == 'O'):
            print(f'\nWin {self.first_player} ')
            return True
        else:
            return False

    def player_change(self):
        if self.first_player == 'X':
            self.first_player = 'O'
        elif self.first_player == 'O':
            self.first_player = 'X'

    def input_check(self):
        while True:
            target = int(input(f'\nХодит {self.first_player} (1-9): '))
            if 1 <= target <= 9:
                return target
            else:
                print(f'Вы ввели {target}.\nВведите число в диапазоне 1-9')


def main():
    board = TicTacToeBoard()
    board.board_print()
    print('\nПервым ходит Х')
    while True:
        target = board.input_check()
        board.step(target)
        if board.win_check():
            break

        # ttt_board.player_change()
        if board.board_check_not_finish():
            print()
            print('Нет свободных мест на поле - Ничья')
            break


if __name__ == '__main__':
    main()

