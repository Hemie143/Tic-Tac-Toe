
def print_state(cells):
    print("---------")
    for y in range(2, -1, -1):
        print(f'| {cells[y][0]} {cells[y][1]} {cells[y][2]} |')
    print("---------")

valid_coords = ["1", "2", "3"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
cells = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_state(cells)

player = ["X", "O"]
turn = 0
while True:
    while True:
        move = input("Enter the coordinates:")
        if " " not in move:
            continue
        else:
            x, y = move.split()
        if not x.isnumeric() and not y.isnumeric():
            print("You should enter numbers!")
        elif x not in valid_coords or y not in valid_coords:
            print("Coordinates should be from 1 to 3!")
        elif cells[int(y) - 1][int(x) - 1] in "XO":
            print("This cell is occupied! Choose another one!")
        else:
            cells[int(y) - 1][int(x) - 1] = player[turn % 2]
            turn += 1
            break
    print_state(cells)

    empty_cell = any([cell == " " for row in cells for cell in row])
    x3 = cells[0] == ["X", "X", "X"] or cells[1] == ["X", "X", "X"] or cells[2] == ["X", "X", "X"] \
         or (cells[0][0] == "X" and cells[1][0] == "X" and cells[2][0] == "X") \
         or (cells[0][1] == "X" and cells[1][1] == "X" and cells[2][1] == "X") \
         or (cells[0][2] == "X" and cells[1][2] == "X" and cells[2][2] == "X") \
         or (cells[0][0] == "X" and cells[1][1] == "X" and cells[2][2] == "X") \
         or (cells[2][0] == "X" and cells[1][1] == "X" and cells[0][2] == "X")
    o3 = cells[0] == ["O", "O", "O"] or cells[1] == ["O", "O", "O"] or cells[2] == ["O", "O", "O"] \
         or (cells[0][0] == "O" and cells[1][0] == "O" and cells[2][0] == "O") \
         or (cells[0][1] == "O" and cells[1][1] == "O" and cells[2][1] == "O") \
         or (cells[0][2] == "O" and cells[1][2] == "O" and cells[2][2] == "O") \
         or (cells[0][0] == "O" and cells[1][1] == "O" and cells[2][2] == "O") \
         or (cells[2][0] == "O" and cells[1][1] == "O" and cells[0][2] == "O")

    if not x3 and not o3 and not empty_cell:
        print("Draw")
        break
    elif x3:
        print("X wins")
        break
    elif o3:
        print("O wins")
        break
