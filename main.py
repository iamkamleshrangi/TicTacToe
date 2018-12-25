#Tic Tac Toe Game
#Author: Kamlesh Kumar Rangi
#Date 25 Dec 2018 

board = [ ' ' for i in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print()
    print()
    print('    |    |')
    print(' ' + str(board[1]) + '  | ' + str(board[2]) + '  | ' + str(board[3]) + ' ')
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[4]) + '  | ' + str(board[5]) + '  | ' + str(board[6]) + ' ')
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + str(board[7]) + '  | ' + str(board[8]) + '  | ' + str(board[9]) + ' ')
    print('    |    |')
    print()
    print()

def isWinner(bo, label):
    return (bo[1] == label and bo[2] == label and bo[3] == label) or (bo[4] == label and bo[5] == label and bo[6] == label) or (bo[7] == label and bo[8] == label and bo[9] == label) or (bo[1] == label and bo[5] == label and bo[9] == label) or (bo[3] == label and bo[5] == label and bo[7] == label) or(bo[1] == label and bo[4] == label and bo[7] == label) or (bo[2] == label and bo[5] == label and bo[8] == label) or (bo[3] == label and bo[6] == label and bo[9] == label)

def isBoardFull(board):
    if board.count(' ') > 1:
        return False 
    else:
        return True

def playerMove():
    run = True 
    while run:
        move = input('Enter Position between 1-9 (X-Player)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run =False
                    insertLetter('X', move)
                else:
                    print('Space Is Already Occupied!')
        except:
            print('Please Enter Vaild Number')

def compMove():
    pass

def main():
    print()
    print('==============================')
    print('===|   TIC TAC TOE GAME   |===')
    print('==============================')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, 'X')):
            playerMove()
            printBoard(board)
        else:
            print('Player X Won the game')
            break

        if not(isWinner(board, 'O')):
            move = compMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O', move)
                print('Computer Place Position to %s'%move)
                printBoard(board)
        else:
            print('Player O Won the game')
            break

        if isBoardFull(board):
            print('Match Is Tie')
main()
