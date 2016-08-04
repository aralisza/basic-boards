class T3Board(object):
    """Represents tic tac toe board"""
    def __init__(self):
        self.board = [[' ', ' ', ' '] for i in range(0,3)]
        self.win = False
        self.turn = 0

    def printBoard(self):
        print "+---+---+---+"
        for row in self.board:
            print "|",
            for piece in row:
                print piece + " |",
            print "\n+---+---+---+"

    def place(self, x, y):
        if x <= 2 and y <= 2 and x >= 0 and y >= 0 and self.board[x][y] == ' ':
            if self.turn % 2 == 0:
                self.board[x][y] = 'x'
            else:
                self.board[x][y] = 'o'
            self.checkWin(x, y)
            self.turn += 1
        else:
            print "invalid move"

    def checkWin(self, x, y):
        if abs(x-y) == 0:
            self.win = self.win or self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '
            if x == 1:
                self.win = self.win or self.board[2][0] == self.board[1][1] == self.board[0][2] != ' '
        elif abs(x-y) == 2:
            self.win = self.win or self.board[2][0] == self.board[1][1] == self.board[0][2] != ' '

        self.win = self.win or self.board[x][0] == self.board[x][1] == self.board[x][2] != ' '
        self.win = self.win or self.board[0][y] == self.board[1][y] == self.board[2][y] != ' '

    def play(self):
        while self.turn < 10 and not self.win:
            self.printBoard()

            if self.turn % 2 == 0:
                print "It's X's turn."
            else:
                print "It's O's turn."

            usr = raw_input("Enter coordinates in form 'row, col': ").split(',')

            if len(usr) == 2:
                self.place(int(usr[0]), int(usr[1]))
            else:
                print "invalid move"

        self.printBoard()
        
        if self.win:
            if self.turn % 2 == 0:
                print "Player O wins!"
            else:
                print "Player X wins!"
        else:
            print "Draw"

T3Board().play()
