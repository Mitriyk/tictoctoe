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
        return all(c == 'X' or c == 'O' for c in self._board )

    def step(self, player, target):
        if self.stepCheck(target):
            self._board[target - 1] = self.first_player
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
            print('\nWin X ', end='')
            return True
        else:
            return False

    def playerChange(self):
        if self.first_player == 'X':
            self.first_player = 'O'
        elif self.first_player == 'O':
            self.first_player = 'X'


def main():
    cell_index = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    X, O, BLANCK = 'X', 'o', '-'
    PLAYERFIRST = 'X'
    ttt_board = TicTacToeBoard()
    ttt_board.boardPrint()
    print('\nПервым ходит Х')
    while True:
        target = int(input(f'\nХодит {ttt_board.first_player} (1-9): '))
        ttt_board.step(PLAYERFIRST, target)

        if ttt_board.winCheck():
            print('Game over')
            break

        if ttt_board.boardCheckNotFinish():
            print()
            print('Нет свободных мест на поле')
            break


if __name__ == '__main__':
    main()
