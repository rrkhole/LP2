class Chessboard:
    def __init__(self,board):
        self.board=board
        self.N=len(board)
        self.ld = [0] * 30
        self.rd = [0] * 30
        self.cl = [0] * 30
    def printSolution(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i][j], end=" ")
            print()

    def solveNQUtil(self, col):
        """ base case
           """
        if (col >= self.N):
            return True

        """ Consider this column and try placing
            this queen in all rows one by one """
        for i in range(self.N):

            if ((self.ld[i - col + self.N - 1] != 1 and
                 self.rd[i + col] != 1) and self.cl[i] != 1):
                board[i][col] = 1
                self.ld[i - col +self.N - 1] = self.rd[i + col] = self.cl[i] = 1

                if (self.solveNQUtil( col + 1)):
                    return True

                self.board[i][col] = 0  # BACKTRACK
                self.ld[i - col + self.N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self):

        if (self.solveNQUtil(0) == False):
            print("Solution does not exist")
            return False
        self.printSolution()
        return True

while True:
    n=int(input("Enter size of board: "))
    board=[]
    for i in range(n):
        board.append([0]*n)

    B=Chessboard(board)
    B.solveNQ()
    print("Do you want to continue playing(Y/N):")
    ch=input()
    if(ch=="N"):
        break
    elif(ch!="Y"):
        print("Enter valid choice")

