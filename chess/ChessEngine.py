class GameState():
    """
    The Chessboard will be represented by list of lists.

    8 x 8 
    representation of the empty space is done by the "0".
    
    """
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ", "bK","bN","bB","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ", "wK","wN","wB","wR"]
        ]
        self.WhiteToMove = True
        self.moveLog = []

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "0"
        self.board[move.endRow][move.endCol] = move.movedPiece

        self.moveLog.append(move)
        self.WhiteToMove = not self.WhiteToMove 

    def undoMove(self):
        """
        !!(NOTE) to undo a move is basically returning the state of the board from where initialy was.

        """
        while(len(self.moveLog) > 0):
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = self.board[move.endRow][move.endCol]
            self.board[move.endRow][move.endCol] =  move.CapturedPiece             
            self.WhiteToMove = not self.WhiteToMove
    
    def PawnMove(self, piece):
        if (piece[1] == "p"):
            ...

    




    def validMoves(self):
        return self.getAllPossibleMoves()


    def getAllPossibleMoves(self) -> dict:
        moves = {}
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                pieceColor = piece[0]
                if pieceColor == 'w' or pieceColor =='b':
                    pieceType = piece[1]
                    if(pieceType =="B"):

                        moves[pieceType] = self.BishopMove(piece)                        
                    if (pieceType == "N"):
                        moves[pieceType] = self.NightMove(piece)
                    elif (pieceType == "Q"):
                        moves[pieceType] = self.QueenMove(piece)
                    
                    elif (pieceType == "K"):
                        moves[pieceType] = self.kingMove(piece)
                    elif (pieceType == "R"):
                        moves[pieceType] = self.RookMove(piece)
                    else :
                        moves[pieceType] = self.PawnMove(piece)
        return moves
    
    def BishopMove(self, piece):
        pass
    

    def NightMove(self, piece):
        pass

    def QueenMove(self, piece):
        pass

    def RookMove(self, piece):
        pass

    def kingMove(self, piece):
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

        if (len(self.movedPiece) == 2 and self.movedPiece[1] != "p"):
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

        return print(f"From square:--> {self.getFilRank(self.startRow, self.startCol)}\t.To square :-->{self.getFilRank(self.endRow, self.endCol)}")
        


        

