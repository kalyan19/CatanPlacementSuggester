import random

class MoveSuggester:

    currentResources = None
    currentValues = None

    def __init__(self, board):
        self.board = board
        self.strategy = 'DIVERSIFY RESOURCE'

    def suggestMove(self):
        possibleMoves = self.board.getLegalMoves()

        if self.strategy == 'RANDOM':
            move = self.randomMove(possibleMoves)
        elif self.strategy == 'GREEDY':
            move = self.greedyMove(possibleMoves)
        elif self.strategy == 'DIVERSIFY RESOURCE':
            move = self.diversifyByResources(possibleMoves)

        return move

    def randomMove(self, possibleMoves):
        move = random.choice(possibleMoves)
        return move

    def greedyMove(self, possibleMoves):
        # for each move, sum up its hexs
        scoreMoves = [(sum([hex.getScore() for hex in move.hexs]), move) for move in possibleMoves]
        bestScoreMove = max(scoreMoves, key=lambda x: x[0])
        return bestScoreMove[1]

    def diversifyByResources(self, possibleMoves):

        if not self.currentResources: # default to greedy when this is the first move
            return self.greedyMove(possibleMoves)

        wantedResources = {"SHEEP", "HAY", "ORE", "WOOD", "BRICK"} - set(self.currentResources)
        # filter for those resources
        movesWithAllResources = []
        movesWithAllButOneResource = []
        movesWithAllButTwoResources = []
        for move in possibleMoves:
            resources = [hex.resource for hex in move.hexs]
            numOfResourcesLeft = len(wantedResources - set(resources))
            if numOfResourcesLeft == 0:
                movesWithAllResources.append(move)
            elif numOfResourcesLeft == 1:
                movesWithAllButOneResource.append(move)
            elif numOfResourcesLeft == 2:
                movesWithAllButTwoResources.append(move)

        print(movesWithAllResources)
        print(movesWithAllButOneResource)
        print(movesWithAllButTwoResources)

        # do greedy with the moves with all/most of the resources
        if movesWithAllResources:
            bestMove = self.greedyMove(movesWithAllResources)
        elif movesWithAllButOneResource:
            bestMove = self.greedyMove(movesWithAllButOneResource)
        elif movesWithAllButTwoResources:
            bestMove = self.greedyMove(movesWithAllButTwoResources)
        else: # default to greedy
            print("Defaulting to greedy...")
            bestMove = self.greedyMove(possibleMoves)
        return bestMove

    def addPreviousMove(self, previousMove):
        self.currentResources = previousMove.getResources()
        self.currentValues = previousMove.getValues()




