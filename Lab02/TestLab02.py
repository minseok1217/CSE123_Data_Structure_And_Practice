from Lab02 import Matrix, EightQueens, TicTacToe

def useMatrix():
    m1 = Matrix(5,5,'r')
    m1.mPrint()
    # m2 = Matrix(5, 5, 'r')
    # m2.mPrint()
    # m = m1 + m2
    # m.mPrint()

def useEightQueens():
    e1 = EightQueens()
    e1.runEQ(8)

def useTicTacToe():
    ttt = TicTacToe()
    ttt.play_ttt()

def main():
    # useMatrix()
    useEightQueens()
    # useTicTac
    # Toe()
    # cat = [[0 for j in range(15)] for i in range(20)]
    # print(cat)
if __name__ == "__main__":
    main()