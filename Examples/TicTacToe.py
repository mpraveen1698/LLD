
####define player 

class Player:
    def __init__(self,name, shape):
        self.name=name 
        self.shape=shape
    
    def get_move(self):
        try:
            input_val=input(f'{self.name} with shape {self.shape}::  Enter the location (row, col) ::    ').strip()
            row, col = map(int, input_val.split(","))
            return row,col 
        except:
            print("Invalid input format. Please enter row,col (e.g., 1,1).")
            return self.get_move()

class Board:
    def __init__(self, size):
        self.size=size
        self.boardgrid=[["" for _ in range(self.size)] for _ in range(self.size)]

    def displayBoard(self):
        for row in self.boardgrid:
            print("|".join (cell if cell else " "  for cell in row))
            print("-"*self.size**2)
    def isValidMove(self,row,col):
        return 0<=row < self.size and 0<=col < self.size and not self.boardgrid[row][col]
    
    def make_move(self, row,col ,shape):
        self.boardgrid[row][col]=shape

    def isfull(self):
        return all(cell for row in self.boardgrid for cell in row)
    
    def check_winner(self, shape):

        #check row wise and col wise:

        for i in range(self.size):
            if all(self.boardgrid[i][j]==shape for j in range(self.size)) or all(self.boardgrid[j][i]==shape for j in range(self.size)):
                return True
        
        if all(self.boardgrid[i][i]==shape for i in range(self.size)) or all(self.boardgrid[i][self.size-1-i]==shape for i in range(self.size)):
                return True
        return False

class Game:
    def __init__(self,boardsize,player1,player2):
        self.board=Board(boardsize)
        self.player1=player1
        self.player2=player2
        self.currentPlayer=player1

    def switch_turn(self):
        self.currentPlayer= self.player1 if self.currentPlayer==self.player2 else self.player2
    
    def play(self):
        print("welcome to the Tic Tac Toe")
        self.board.displayBoard()

        while True:
            row, col =self.currentPlayer.get_move()
            if self.board.isValidMove(row,col):
                self.board.make_move(row,col,self.currentPlayer.shape)
                self.board.displayBoard()
                if self.board.check_winner(self.currentPlayer.shape):
                    print(f"Congrats !!!!  Winner {self.currentPlayer.name}")
                    return
                if self.board.isfull():
                    print("Its a Draw!!!")
                    return
                self.switch_turn()
            else:
                print("Its a invalid move !! please try again")

if __name__=='__main__':
    Player1=Player("P1","X")
    Player2=Player("P2","O")
    game=Game(3,Player1,Player2)
    game.play()

    