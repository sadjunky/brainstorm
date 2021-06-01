
def initialize(n):
    for key in ['row', 'col', 'nwtose', 'swtone']:
        board[key] = {}
    for i in range(n):
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1), n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0

def printboard():
    for pos in queen: 
        print((pos[0], pos[1]), end=" ")
    print(" ")

def free(i, j):
    return (board['row'][i] == 0 and board['col'][j] == 0 and board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i, j):
    queen.append((i, j))
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][j+i] = 1

def undoqueen(i, j):
    queen.pop()
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0

def placequeen(i):
    for j in range(n):
        if free(i, j): # Check if position is not attacked
            addqueen(i, j)
            if i == n - 1: # Reached end of rows in the board
                printboard()
            else:
                placequeen(i+1) # This solution extends fully
            undoqueen(i, j)


board = {}
queen = []
n = int(input("How many queens? "))
initialize(n)
placequeen(0)
