class Player:
    def __init__(self):
        self.row = [0, 0, 0]
        self.col = [0, 0, 0]
        self.diagonal = 0
        self.semi_diagonal = 0

    def won(self):
        return max(self.row) == 3 or \
               max(self.col) == 3 or \
               self.diagonal == 3 or \
               self.semi_diagonal == 3

    def update(self, new_row, new_col):
        self.col[new_col] += 1
        self.row[new_row] += 1
        if (new_row, new_col) in ((0, 0), (1, 1), (2, 2)):
            self.diagonal += 1
        if (new_row, new_col) in ((0, 2), (1, 1), (2, 0)):
            self.semi_diagonal += 1


class TicTac:
    def __init__(self, testing_array=None):
        self.step = 0
        self.matrix = [[-1 for _ in range(3)] for _ in range(3)]
        self.player_x = Player()
        self.player_0 = Player()
        self.last_sell_rewriting_attempt = ''
        self.testing_array = testing_array

    def hello(self):
        if not self.testing_array:
            print('''Input row, column separated by whitespace.
To show current situation type "show board"

012
0|---
1|---
2|---
''')
        else:
            print(f'{self.testing_array=}')

    def input_analysis(self, text_users_input):
        users_input = text_users_input.split()
        result = {'is_valid': False}
        if users_input and users_input[0] == 'show':
            self.show_board()
            result['message'] = 'Good luck!'
            return result

        if len(users_input) != 2:
            result['message'] = '2 coordinates expected. '
        elif not all(x.isdigit() for x in users_input):
            result['message'] = 'Digits expected. '
        else:
            row, col = map(int, users_input)
            if not 0 <= row <= 2 or not 0 <= col <= 2:
                result['message'] = 'Numbers between 0 and 2 expected. '
            elif self.matrix[row][col] != -1:
                result['message'] = 'Cell is filled. '
                self.last_sell_rewriting_attempt = text_users_input
            else:
                result['is_valid'] = True
                result['content'] = (row, col)
        if 'message' in result:
            result['message'] += 'Try again.'
        return result

    def show_board(self):
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                    print('0', end='')
                elif self.matrix[i][j] == 1:
                    print('X', end='')
                else:
                    print('-', end='')
            print()
        print('*****')

    def start_game(self, test_i=0):
        self.hello()
        while self.step < 9:
            if not self.testing_array:
                users_input = input()
            else:
                if test_i == len(self.testing_array):
                    break
                users_input = self.testing_array[test_i]
                test_i += 1
            analysis_result = self.input_analysis(users_input)
            if analysis_result['is_valid']:
                row, col = analysis_result['content']
                if self.step % 2 == 0:
                    self.matrix[row][col] = 1
                    self.player_x.update(row, col)
                else:
                    self.matrix[row][col] = 0
                    self.player_0.update(row, col)
                self.step += 1
                self.show_board()
                if self.player_x.won():
                    return 'X won'
                if self.player_0.won():
                    return '0 won'
            else:
                if not self.testing_array:
                    print(analysis_result['message'])
        else:
            return 'Draw'


if __name__ == "__main__":
    game = TicTac()
    print('*********')
    print(f'* {game.start_game()} *')
    print('*********')
