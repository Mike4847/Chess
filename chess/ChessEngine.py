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
        self.ChessNotation = {"Knight":"K", "Rook":"R", "King": "K", "Queen":"Q", "Bishop": "B"}

        self.movedPiece = board[self.startRow][self.startCol]
        self.toPiece = board[self.endRow][self.endCol]

    def getFilRank(self, row , column):
        return self.colToFile[column] + self.rowToRank[row]



    def getChessNotation(self):
        return self.getFilRank(self.startRow, self.startCol) +  self.getFilRank(self.endRow, self.endCol)
        


        

