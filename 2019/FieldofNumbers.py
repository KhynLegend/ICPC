import re
text = ''

for line in range(9):
    text += input() + "\n"

board = text.split('\n')

for i in range(len(board)):
    board[i] = list(map(int, board[i].split()))

isSudoku = []

#checkColumns
for i in range(len(board)):
    if any([re.match('[0-9]', str(j)) and (j <= 9 and j >= 0) for j in board[i]]):
        #check row duplicates
        for j in range(len(board[i])):
            for x in range(len(board[i])):
                if board[i][x] == board[i][j] and x != j:
                    print('Sad Aku.')
                    exit()
        isSudoku.append(True)
    
print('Sudoku' if any(isSudoku) else 'Sad Aku.')

