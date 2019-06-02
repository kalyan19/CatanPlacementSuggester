from Board import Board
from MoveSuggester import MoveSuggester


board = Board()
moveSuggester = MoveSuggester(board)
suggestedMove1 = moveSuggester.suggestMove()
print("Suggester first move is {}".format(suggestedMove1))
board.acceptMove(suggestedMove1)
print(suggestedMove1.getScore())

moveSuggester.addPreviousMove(suggestedMove1)
suggestedMove2 = moveSuggester.suggestMove()
print("Suggester second move is {}".format(suggestedMove2))
board.acceptMove(suggestedMove2)
print(suggestedMove2.getScore())

