grid = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."]
]

player = 0


def print_grid():
    for row in grid:
        print("|" + " ".join(row) + "|")
    print(" ------------- ")
    print(" 0 1 2 3 4 5 6 ")


def check_win(piece):
    rows = 6
    cols = 7

 
    for r in range(rows):
        for c in range(cols - 3):
            if all(grid[r][c+i] == piece for i in range(4)):
                return True

    
    for r in range(rows - 3):
        for c in range(cols):
            if all(grid[r+i][c] == piece for i in range(4)):
                return True

   
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(grid[r+i][c+i] == piece for i in range(4)):
                return True

    
    for r in range(rows - 3):
        for c in range(3, cols):
            if all(grid[r+i][c-i] == piece for i in range(4)):
                return True

    return False


def is_draw():
    return all(grid[0][c] != "." for c in range(7))


while True:
    print_grid()

    if player == 0:
        piece = "X"
        print("\nPLAYER ONE'S TURN")
    else:
        piece = "O"
        print("\nPLAYER TWO'S TURN")

    try:
        column = int(input("Choose column"))
        if column < 0 or column > 6:
            print("Invalid column. Try again.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

   
    if grid[0][column] != ".":
        print("Column is full. Try another one.")
        continue

   
    for i in range(6):
        if grid[-(i+1)][column] == ".":
            grid[-(i+1)][column] = piece
            break

   
    if check_win(piece):
        print_grid()
        if player == 0:
            print("PLAYER ONE WINS!")
        else:
            print("PLAYER TWO WINS!")
        break

    
    if is_draw():
        print_grid()
        print("It's a draw!")
        break

  
    player = 1 - player