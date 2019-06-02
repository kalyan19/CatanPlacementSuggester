import random

class MoveSuggester:

    def __init__(self, board):
        self.board = board
        self.strategy = 'GREEDY'

    def suggestMove(self):
        possibleMoves = self.board.getLegalMoves()

        if self.strategy == 'RANDOM':
            move = self.randomMove(possibleMoves)
        elif self.strategy == 'GREEDY':
            move = self.greedyMove(possibleMoves)

        return move

    def randomMove(self, possibleMoves):
        move = random.choice(possibleMoves)
        return move

    def greedyMove(self, possibleMoves):
        # for each move, sum up its hexs
        scoreMoves = [(sum([hex.getScore() for hex in move.hexs]), move) for move in possibleMoves]
        bestScoreMove = max(scoreMoves, key=lambda x: x[0])
        return bestScoreMove[1]





