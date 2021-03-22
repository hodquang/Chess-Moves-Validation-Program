import Helpers
import ChessEngine
import ChessBoard

def main():
	board_state = [
		"WHITE: Rf1, Kg1, Pf2, Ph2, Pg3, Qf5",
		"BLACK: Kb8, Ne8, Pa7, Pb7, Pc7, Ra5", 
		"PIECE TO MOVE: Rf1"]
	data = Helpers.getInput(board_state)
	print(data)
	target = data[2]
	board = ChessBoard.drawPieces(data)
	color = Helpers.findColor(data)
	moves = ChessEngine.getValidMoves(board, target, color)
	print("Input:")
	for i in board_state:
		print(i)
	print('LEGAL MOVES FOR {}: {}'.format(target, ", ".join(moves)))


if __name__ == "__main__":
	main()
