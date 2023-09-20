game = [[" " for _ in range(3)] for _ in range(3)]
def zona_game(game):
    for row in game:
        print(" | ".join(row))
        print("-" * 9)

def check_win(game, player):
    for i in range(3):
        if all(game[i][j] == player for j in range(3)) or \
           all(game[j][i] == player for j in range(3)):
            return True
    if all(game[i][i] == player for i in range(3)) or \
       all(game[i][2-i] == player for i in range(3)):
        return True
    return False

current_player = "X"
moves = 0
while True:
    zona_game(game)
    print(f"Ход игрока {current_player}")
    row = int(input("Введите номер строки (1, 2, 3): ")) - 1
    col = int(input("Введите номер столбца (1, 2, 3): ")) - 1

    if 0 <= row < 3 and 0 <= col < 3 and game[row][col] == " ":
        game[row][col] = current_player
        moves += 1
        if check_win(game, current_player):
            zona_game(game)
            print(f"Игрок {current_player} победил!")
            break
        elif moves == 9:
            zona_game(game)
            print("Ничья!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Уже занято!")
