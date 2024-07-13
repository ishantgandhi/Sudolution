from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    data = request.get_json()
    board = data['board']

    original_board = [row.copy() for row in board]  

    if solve(board):
        return jsonify({"solvedBoard": board})
    else:
        return jsonify({"error": "No solution exists"}), 400

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
    b_x = p[1] // 3
    b_y = p[0] // 3
    for i in range(b_y * 3, b_y * 3 + 3):
        for j in range(b_x * 3, b_x * 3 + 3):
            if b[i][j] == n and (i, j) != p:
                return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
