class ChessEngine():
    """
    The Chessboard will be represented by list of lists.

    8 x 8 
    representation of the empty space is done by the "0".
    
    """
    def __int__(self):
        self.board = [
            ["bR","bB","bN","bQ", "bK","bN","bB","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wB","wN","wQ", "wK","wN","wB","wR"]
        ]


        