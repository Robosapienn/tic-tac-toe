import random

gameBoard = ["─", "─", "─",
             "─", "─", "─",
             "─", "─", "─"]
currentPlayer = "X"
winner = None
gameRun = "Y"


def printBoard(board):
    print("┌───┬───┬───┐")
    print("│ " + board[0] + " │ " + board[1] + " │ " + board[2] + " │")
    print("├───┼───┼───┤")
    print("│ " + board[3] + " │ " + board[4] + " │ " + board[5] + " │")
    print("├───┼───┼───┤")
    print("│ " + board[6] + " │ " + board[7] + " │ " + board[8] + " │")
    print("└───┴───┴───┘")


def playerInput(board):
    choice = int(input("Enter a number between 1-9:"))
    while choice < 1 or choice > 9 or board[choice - 1] != "─":
        print("Invalid entry. Choose another number.")
        choice = int(input("Enter a number between 1-9:"))
    board[choice - 1] = "X"


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "─":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "─":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "─":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "─":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "─":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "─":
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "─":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "─":
        winner = board[2]
        return True


def checkTie(board):
    global gameRun
    if "─" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRun = input("Play again Y/N?\n")
        if gameRun == "Y":
            resetBoard()
        else:
            gameRun = None


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def checkWin():
    global gameRun
    if (checkHorizontal(gameBoard) or
        checkVertical(gameBoard) or
        checkDiagonal(gameBoard)):
        printBoard(gameBoard)
        if winner == "O":
            print("The robots have taken over the world!")
        else:
            print("Humanity wins!")
        gameRun = input("Play again Y/N?\n")
        if gameRun == "Y":
            resetBoard()
        else:
            gameRun = None


def resetBoard():
    global currentPlayer
    global winner
    global gameBoard
    gameBoard = ["─", "─", "─",
                 "─", "─", "─",
                 "─", "─", "─"]
    if winner == "O":
        currentPlayer = "X"
    elif winner == "X" or winner == None:
        currentPlayer = "O"
    winner = None


def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "─":
            board[position] = "O"
            switchPlayer()


while gameRun == "Y":
    printBoard(gameBoard)
    playerInput(gameBoard)
    checkWin()
    checkTie(gameBoard)
    switchPlayer()
    computer(gameBoard)
    checkWin()
    checkTie(gameBoard)

