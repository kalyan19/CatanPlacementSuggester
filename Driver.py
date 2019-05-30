from Board import Board
from MoveSuggester import MoveSuggester


board = Board()
moveSuggester = MoveSuggester(board)
suggestedMove = moveSuggester.suggestMove()
print("Suggester suggests move {}".format(suggestedMove))



