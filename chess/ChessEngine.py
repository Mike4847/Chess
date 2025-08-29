class GameState():
    """
    The Chessboard will be represented by list of lists.

    8 x 8 
    representation of the empty space is done by the "0".
    
    """
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ", "bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "bp", "0", "0", "0", "0"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ", "wK","wB","wN","wR"]
        ]
        self.WhiteToMove = True
        self.moveLog = []
        self.pieceFunction = {"B": self.BishopMove, "K": self.kingMove, "Q":self.QueenMove, "p": self.PawnMove, "N": self.KNightMove, "R":self.RookMove}
        

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "0"
        self.board[move.endRow][move.endCol] = move.movedPiece

        self.moveLog.append(move)
        self.WhiteToMove = not self.WhiteToMove 

    def undoMove(self):
        """
        !!(NOTE) to undo a move is basically returning the state of the board from what initialy was.

        """
        if(len(self.moveLog) > 0):

            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = self.board[move.endRow][move.endCol]
            self.board[move.endRow][move.endCol] =  move.CapturedPiece             
            self.WhiteToMove = not self.WhiteToMove
    
    def PawnMove(self,row, col, move):
        if (self.board[row][col][0] == "w"): #white attack moves
            #check if the 
            if (self.board[row-1][col] == "0"):
                move.append(Move((row, col), (row - 1, col), self.board))
                if (row== 6 and self.board[row - 2][col] == "0"):
                    move.append(Move((row, col), (row - 2, col), self.board))
            if ((col + 1) <= len(self.board)): # check for right captures 
                if(self.board[row - 1][col + 1][0] == "b"):
                    move.append(Move((row, col), (row-1, col + 1), self.board))
            if (col - 1>= 0):# check for left captures
                if(self.board[row][col - 1][0] == "b"):
                    move.append(Move((row, col), (row-1, col - 1), self.board))
        else: #implementing the black moves
            if (row + 1) > len(self.board): # move one step forward
                move.append((row, col), (row + 1, col))
                if row == 1 and self.board[row+2][col] == "0": # but whatif its a pawns first move and the path is clear ... move twice!!
                    move.append((row, col),(row + 2, col))
            # NOTE(CAPTURES)
            if (col + 1) >=0 and self.board[row + 1][col + 1][0] =="w":     # right captures
                move.append(Move((row , col), (row+1,col+1), self.board))
            if ()



            

                  




    def validMoves(self)->dict:
        return self.getAllPossibleMoves()


    def getAllPossibleMoves(self) -> list:
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if((self.board[row][col][0] == "w" and self.WhiteToMove ) or (self.board[row][col][0] == "b" and not self.WhiteToMove ) ):
                    #piece = self.board[r][c]
                    self.pieceFunction[self.board[row][col][1]](row, col, moves)
                
        return moves
    
    def BishopMove(self,row , col, move):
        if self.board[row][col][0] == "w": #white move
            
    
    

    def KNightMove(self,row , col, move):
        pass

    def QueenMove(self, row , col, move):
        pass

    def RookMove(self, row , col, move):
        pass

    def kingMove(self, row , col, move):
        pass


class Move():
    RanksToRow= {"8": 0, "7":1, "6":2, "5":3, "4":4, "3":5, "2":6, "1":7, "0":8}
    rowToRank = { v: k for k, v in RanksToRow.items()}

    fileToCol = {"a": 0 , "b":1 , "c":2, "d":3 , "e":4, "f":5, "g":6, "h":7}
    colToFile= { v: k for k, v in fileToCol.items()}

    def __init__(self , board , sqStart, sqEnd):
        self.startRow = sqStart[0]
        self.startCol = sqStart[1]
        self.endRow = sqEnd[0]
        self.endCol = sqEnd[1]
        
        self.movedPiece = board[self.startRow][self.startCol]
        self.CapturedPiece = board[self.endRow][self.endCol]
        self.PieceNotation = ""
        #attach a unique identifier
        self.MoveId = self.startCol *10000 + self.endCol * 1000 + self.endRow*100
        self.PieceNotation = self.movedPiece[1]
        



        #if(switch)


    def getFilRank(self,Endrow , Endcol):
        """
        the standard naming accepted by FIDE(algebraic notation-- though it a misnomer!!):
        'E1' <file, rank >
        rank refers to the list of horizontal square in the chess board.
        file refers to the list of vertical square in the chess board.
        """
        return self.colToFile[Endcol] + self.PieceNotation +self.rowToRank[Endrow]
    

    def getChessNotation(self, board):
        """
        i am gonna try as much as possible to keep the notation as the : ALGEBRA NOTATION
        """

        return print(f"From square:--> {self.getFilRank(self.startRow, self.startCol)} {self.PieceNotation}\t.To square :-->{self.getFilRank(self.endRow, self.endCol)}{self.PieceNotation}")
        


        

