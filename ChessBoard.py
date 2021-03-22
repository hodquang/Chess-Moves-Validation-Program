import sys
import Helpers

def drawPieces(List):
	if Helpers.validateInput(List) is False: sys.exit("Not a proper board")
	board = [
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]]
	white = List[0]
	black = List[1]
	# We will load the pieces into our board. 
	# White will be the bottom player, and black will be the top. 
	# White pawns move upward and black pawns move downward.
	for piece in white:
		board[int(piece[2]) - 1][Helpers.charToNum(piece[1]) - 1] = 'w' + piece[0]
	for piece in black:
		board[int(piece[2]) - 1][Helpers.charToNum(piece[1]) - 1] = 'b' + piece[0]
	return board[::-1]
