import random

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ship:
    def __init__(self, length):
        self.length = length
        self.dots = []

class Board:
    def __init__(self):
        self.board = [['O' for _ in range(6)] for _ in range(6)]
        self.ships = []

    def show(self, hide_ships=False):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        print("-" * 29)
        for i, row in enumerate(self.board):
            row_str = f"{i + 1} | "
            for j, cell in enumerate(row):
                if hide_ships and cell == '■':
                    row_str += 'O | '
                else:
                    row_str += f"{cell} | "
            print(row_str)
            print("-" * 29)

    def add_ship(self, ship):
        if self.valid_placement(ship):
            for dot in ship.dots:
                self.board[dot.x][dot.y] = '■'
            self.ships.append(ship)
            return True
        return False

    def valid_placement(self, ship):
        for dot in ship.dots:
            if not (0 <= dot.x < 6 and 0 <= dot.y < 6) or self.board[dot.x][dot.y] == '■':
                return False
        return True

    def random_board(self):
        ships = [3, 2, 2, 1, 1, 1, 1]

        for ship_length in ships:
            while True:
                x = random.randint(0, 5)
                y = random.randint(0, 5)
                direction = random.choice(['horizontal', 'vertical'])
                ship = self.create_ship(ship_length, x, y, direction)
                if self.add_ship(ship):
                    break

    def create_ship(self, length, x, y, direction):
        ship = Ship(length)
        for i in range(length):
            if direction == 'horizontal':
                dot = Dot(x + i, y)
            else:
                dot = Dot(x, y + i)
            ship.dots.append(dot)
        return ship

class Game:
    def __init__(self):
        self.player_board = Board()
        self.bot_board = Board()
        self.player_board.random_board()
        self.bot_board.random_board()

    def start(self):
        print("Приветствую в моей игре!)")
        while True:
            self.show_boards(hide_ships=True)
            self.player_move()
            if self.check_end():
                break
            self.bot_move()
            if self.check_end():
                break

    def show_boards(self, hide_ships=False):
        print("Моё поле:")
        self.player_board.show()
        print("\nПоле соперника:")
        self.bot_board.show(hide_ships)

    def player_move(self):
        while True:
            try:
                x, y = map(int, input("Введите номер строки и столбца (1-6), через пробел: ").split())
                if 1 <= x <= 6 and 1 <= y <= 6:
                    target = Dot(x - 1, y - 1)
                    if self.bot_board.board[target.x][target.y] == '■':
                        print("Попадание!")
                        self.bot_board.board[target.x][target.y] = 'X'
                    else:
                        print("Промах!")
                        self.bot_board.board[target.x][target.y] = '.'
                    break
                else:
                    print("Ошибка: Введите два целых числа от 1 до 6, через пробел.")
            except ValueError:
                print("Ошибка: Введите два целых числа от 1 до 6, через пробел.")

    def bot_move(self):
        while True:
            x, y = random.randint(0, 5), random.randint(0, 5)
            target = Dot(x, y)
            if self.player_board.board[target.x][target.y] == '■':
                print("Противник попал в корабль!")
                self.player_board.board[target.x][target.y] = 'X'
            else:
                print("Противник промахнулся!")
                self.player_board.board[target.x][target.y] = '.'
            break

    def check_end(self):
        for ship in self.bot_board.ships:
            if all(self.player_board.board[dot.x][dot.y] == 'X' for dot in ship.dots):
                print("Победа!")
                return True
        return False

if __name__ == "__main__":
    game = Game()
    game.start()
