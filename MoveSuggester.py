import random

class MoveSuggester:

    def __init__(self, board):
        self.board = board
        self.strategy = 'RANDOM'

    def suggestMove(self):
        possibleMoves = self.board.getLegalMoves()

        if self.strategy == 'RANDOM':
            move = self.randomMove(possibleMoves)

        return move

    def randomMove(self, possibleMoves):
        move = random.choice(possibleMoves)
        return move




