from constants.constants import BOARD_SIZE, TALLYS, VALID_POSITIONS
from enums.moves import Moves


class Board:
    def __init__(self) -> None:
        self.state = [[None, None, None], [None, None, None], [None, None, None]]
        self.validMoves = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.winTally = {
            'rows': [0] * BOARD_SIZE,
            'cols': [0] * BOARD_SIZE,
            'diagx': 0,
            'diagy': 0,
        }

    def getBoardObj(board):
        boardObj = Board()
        for position, mark in enumerate(board):
            if mark != None:
                boardObj.markMove(VALID_POSITIONS[position+1], mark, TALLYS[mark])
        return boardObj

    
    def getValidMoves(self):
        flattened = sum(self.validMoves, [])
        # the valid moves as a flattened list with None values removed
        return list(filter(None, flattened))

    def isFull(self):
        return len(self.getValidMoves()) == 0

    def markMove(self, coordinates, mark, tally):
        x, y = coordinates
        self.state[x][y] = mark
        self.validMoves[x][y] = None
        self.winTally['rows'][x] += tally
        self.winTally['cols'][y] += tally
        if x == y:
            self.winTally['diagx'] += tally
        if x + y == BOARD_SIZE - 1:
            self.winTally['diagy'] += tally
    
    def undoMove(self, move, tally):
        x, y = VALID_POSITIONS[move]
        self.state[x][y] = None
        self.validMoves[x][y] = move
        self.winTally['rows'][x] -= tally
        self.winTally['cols'][y] -= tally
        if x == y:
            self.winTally['diagx'] -= tally
        if x + y == BOARD_SIZE - 1:
            self.winTally['diagy'] -= tally

    def getWinner(self):
        winTally = self._getWinnerTallys()
        if not winTally:
            return None
        if winTally > 0:
            return Moves.X.value
        else:
            return Moves.O.value
    
    def _getWinnerTallys(self):
        results = [
            self._getWinnerTallysRowOrCols(self.winTally['rows']),
            self._getWinnerTallysRowOrCols(self.winTally['cols']),
            self._getWinnerTallysDiag(self.winTally['diagx']),
            self._getWinnerTallysDiag(self.winTally['diagy']),
        ]
        # returns the first non-None result or None if all are None
        return next((item for item in results if item is not None), None) 


    def _getWinnerTallysRowOrCols(self, rowsOrCols):
        for tallys in rowsOrCols:
            if abs(tallys) == BOARD_SIZE:
                return tallys
        return None

    def _getWinnerTallysDiag(self, diag):
        if abs(diag) == BOARD_SIZE:
            return diag
        else:
            return None 