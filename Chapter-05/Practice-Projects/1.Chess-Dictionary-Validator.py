# Chess Dictionary Validator

# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 
# to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and 
# returns True or False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can 
# only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; 
# that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has 
# resulted in an improper chess board.
from collections import Counter

def isValidChessBoard(chessBoard):
    identifier = 0
    count = dict(Counter(chessBoard.values()))
    if count['wking'] != 1 or count['bking'] != 1:
        identifier = 0
        return False
    else:
        identifier = 1
    if 'bpawns' in count or 'wpawns' in count:
        if count['bpawns'] > 8 or count['wpawns'] > 8:
            identifier = 0
            return False
        else:
            identifier = 1
    pieceNumber = 0
    for x,y in count.items():
        pieceNumber+=y
    if pieceNumber > 16:
        identifier = 0
        return False
    else:
        identifier = 1
    for x,y in chessBoard.items():
        k = list(x)
        if len(k) != 2:
            identifier = 0
            return False
        else:
            identifier = 1
            if int(k[0]) < 1 or int(k[0]) > 8:
                identifier = 0
                return False
            else:
                identifier = 1
                if k[1] not in ['a','b','c','d','e','f','g','h']:
                    identifier = 0
                    return False
                else:
                    identifier = 1
    if identifier == 1:
        return True