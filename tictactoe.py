class TicTacToe():
    def __init__(self, board):
        self.board = board

    def rowCheck(self, board):
        for row in range(len(board)):
            rows = []
            for col in range(len(board)):
                if board[row][col] != "-":
                    rows.append(board[row][col])
            if len(rows) == 3:
                if len(set(rows)) == 1:
                    return rows[0]
        return False

    def checkCol(self, board):
        for row in range(len(board)):
            rows = []
            for col in range(len(board[0])):
                if board[col][row] != "-":
                    rows.append(board[col][row])
            if len(rows) == 3:
                if len(set(rows)) == 1:
                    return rows[0]
        return False

    def checkFirstDiagonal(self, board):
        rows = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == col:
                    if board[row][col] != "-":
                        rows.append(board[row][col])
        if len(rows) == 3:
            if len(set(rows)) == 1:
                return rows[0]
        return False

    def checkSecondDiagonal(self, board):
        r, c = 0, len(board) - 1
        rows = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == r and col == c:
                    if board[row][col] != "-":
                        rows.append(board[row][col])
            r += 1
            c -= 1
        if len(rows) == 3:
            if len(set(rows)) == 1:
                return rows[0]
        return False

    def printBoard(self, board):
        for row in board:
            for col in row:
                print(col,"|",end=" ")
            print()
            print("-----------")

    def checkWin(self, board):
        result1 , result2 = self.rowCheck(board) , self.checkCol(board)
        result3 , result4 = self.checkFirstDiagonal(board) , self.checkSecondDiagonal(board)
        if result1 != False:
            print(result1, "wins.")
            return True
        if result2 != False:
            print(result2, "wins.")
            return True
        if result3 != False:
            print(result3, "wins.")
            return True
        if result4 != False:
            print(result4, "wins")
            return True

    def Main(self):
        count = 0
        self.printBoard(self.board)
        print("This game consist of 2 players.The first player symbol is X and second player symbol is O.Row and column values can be 1,2 or 3.")
        gameRunning = True
        while gameRunning:
            player1 = input("It's player 1 turn.Enter the row and column of the position where you want to place your symbol separated by space:").split()
            self.board[int(player1[0]) - 1][int(player1[1]) - 1] = "X"
            count += 1
            self.printBoard(self.board)
            if self.checkWin(self.board):
                break
            player2 = input("It's player 2 turn.Enter the row and column of the position where you want to place your symbol separated by space:").split()
            self.board[int(player2[0]) - 1][int(player2[1]) - 1] = "O"
            count += 1
            self.printBoard(self.board)
            if self.checkWin(self.board):
                break
            if count == 8:
                print("No one wins.")
                break

obj = TicTacToe([["-","-","-"],
                ["-","-","-"],
                ["-","-","-"]])
obj.Main()
