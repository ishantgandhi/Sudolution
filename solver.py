board = []
original_board = []
for i in range(9):
    row = input(f"Enter row {i + 1} (use 0 for empty cells and don't space between the numbers): ")
    board.append([int(num) for num in row])

def board_disp(b):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - - ') 
        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ") 
            if j == 8:
                print(b[i][j]) 
            else:
                print(str(b[i][j]) + ' ', end=" ") 

original_board = board.copy()

def solve(b):
    find = search_empty(b)
    if not find:
        return True 
    else:
        row, col = find 
    for n in range(1, 10):
        if check(b, n, (row, col)):
            b[row][col] = n
            if solve(b):
                return True
            b[row][col] = 0
    return False

def search_empty(b):
    for i in range(len(b)): 
        for j in range(len(b[0])): 
            if b[i][j] == 0:
                return (i, j) 
    return None

def check(b, n, p):
    for i in range(len(b[0])): 
        if (b[p[0]][i] == n and p[1] != i): 
            return False
    for i in range(len(b)): 
        if b[i][p[1]] == n and p[0] != i: 
            return False
    b_x = p[1]//3 
    b_y = p[0]//3 
    for i in range(b_y*3, b_y*3 + 3): 
        for j in range(b_x*3, b_x*3+3): 
            if b[i][j] == n and (i,j) != p:
                return False
    return True

def result_disp(b,ob):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - - ') 
        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ") 
            if j == 8:
                if b[i][j] != ob[i][j]:
                    print(f"\033[92m{b[i][j]}\033[0m")
                else:
                    print(b[i][j]) 
            else:
                if b[i][j] != ob[i][j]:
                    print(f"\033[92m{b[i][j]}\033[0m", end=" ")
                else:
                    print(str(b[i][j]) + ' ', end=" ") 

print("Original board:")
board_disp(board)
solve(board)
print("- -"*25)
print("Solved board:")
result_disp(board,original_board)

