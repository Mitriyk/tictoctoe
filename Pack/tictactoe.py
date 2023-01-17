class TicTacToeBoard():
    def __init__(self):
        # self.cells = cells
        # self.
        self.first_player = 'X'
        # self.O = O
        self.BLANCK = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
        self._board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        # for i in self.cells:

    def boardPrint(self):
        for i in range(9):
            print(self._board[i], sep='', end='  ')
            if i == 2 or i == 5:
                print()

    def boardCheckNotFinish(self) -> bool:
        return all(c == 'X' or c == 'O' for c in self._board)

    def step(self, target):
        if self.stepCheck(target):
            self._board[target - 1] = self.first_player
            self.winCheck()
            self.playerChange()

        else:
            print('Место занято - выбери другое!')
        self.boardPrint()

    def stepCheck(self, target) -> bool:
        if self._board[target - 1] not in ['X', 'O']:
            return True
        else:
            return False

    def winCheck(self) -> bool:
        x = self._board
        if (x[0] == 'X' and x[1] == 'X' and x[2] == 'X'
                or x[3] == 'X' and x[4] == 'X' and x[5] == 'X'
                or x[6] == 'X' and x[7] == 'X' and x[8] == 'X'
        ):
            print(f'\nWin {self.first_player} ', end='')
            return True
        else:
            return False

    def playerChange(self):
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
    ttt_board = TicTacToeBoard()
    ttt_board.boardPrint()
    print('\nПервым ходит Х')
    while True:
        target = ttt_board.input_check()
        ttt_board.step(target)
        # if ttt_board.winCheck():
        #     print('Game over')
        #     break
        if ttt_board.boardCheckNotFinish():
            print()
            print('Нет свободных мест на поле')
            break


if __name__ == '__main__':
    main()
