import random

class Matrix:
    rnb = random.Random()
    def __init__(self,rows,cols,f='r'):
        self.M=[]
        while len(self.M) < rows:
            self.M.append([])
            self.M=[]
            if(f=='r'):
                self.rMatrix(rows,cols)
            elif(f=='z'):
                self.zMatrix(rows,cols)

    def rMatrix(self,rows,cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(Matrix.rnb.randint(1, 10))

    def zMatrix(self,rows,cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(Matrix.rnb.randint(1, 10))

    def mPrint(self):
        for rows in self.M:
            print([x for x in rows])

    def __str__(self):
        matrix_str = "\n".join(["\t".join(map(str, row)) for row in self.M])
        return matrix_str

    def __repr__(self):
        return f"Matrix({len(self.M)}, {len(self.M[0])}, 'z')"

    def __add__(self,other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA,colsA,'z')
        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] + other.M[row][col]
        return C

    def __sub__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')
        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] - other.M[row][col]
        return C

    def __mul__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        rowsB = len(other.M)
        colsB = len(other.M[0])
        if colsA != rowsB:
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        C = Matrix(rowsA, colsB, 'z')
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    C.M[i][j] += self.M[i][k] * other.M[k][j]
        return C

    def transpose(self):
        rows = len(self.M)
        cols = len(self.M[0])
        C = Matrix(cols, rows, 'z')
        for i in range(rows):
            for j in range(cols):
                C.M[j][i] = self.M[i][j]
        return C

class EightQueens:
    rnb =random.Random()
    def __init__(self):
        self.bd=list(range(8))

    def runEQ(self, nos):
        found = 0
        tries = 0
        while found < nos :
            EightQueens.rnb.shuffle(self.bd)
            tries += 1
            if not self.has_clashes():
                found+=1
                print(" Solution : {}, {}, {}".format(found, self.bd, tries))
                tries = 0

    def has_clashes(self):
        for col in range(1,len(self.bd)):
            if self.col_clashes(col):
                return True
        return False

    def col_clashes(self,k):
        for i in range(k):
            if self.dclashes(i,self.bd[i], k, self.bd[k]):
                return True
        return False

    def dclashes(self,x0,y0,x1,y1):
        d1 = abs(x0 - y0)
        d2 = abs(x1 - y1)
        return d1==d2

class TicTacToe:
    def __init__(self):
        self.board=[]
        for i in range(9):
            self.board.append(-1)

    def play_ttt(self):
        win = False
        move = 0
        while not win:
            self.printBoard()
            if move % 2 == 0:
                turn = 'X'
            else:
                turn = 'O'
            print("Turn for player : {}".format(turn))

            user = self.getInput(turn)
            while self.board[user] != -1:
                print("Invalid input")
                user = self.getInput(turn)

            self.board[user] = 1 if turn == "O" else 0
            move+=1
            if move > 3:
                winner = self.check_win()
                if winner != -1:
                    print ("The winner is {}".format("x" if winner==1 else "0"))
                    self.quit_game()

    def getInput(self,turn):
        # print("Player{}'s turn".format(turn))
        return eval(input("input one numver between 1 and 9 : "))
        # return eval(input())

    def check_win(self):
        win_cord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,8))
        for each in win_cord:
            if self.board[each[0]]==self.board[each[1]] and self.board[each[1]]==self.board[each[2]]:
                return self.board[each[0]]
            return -1

    def printBoard(self):
        for i in range(0,9):
            print(self.board[i], end=' ')
            if(i % 3 == 2):
                print()
        # print()

    def quit_game(self):
        exit(0)