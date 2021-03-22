import ChessBoard
import ChessEngine
import Helpers

def test_getInput():
	# Create the correct input
	assert Helpers.getInput([
		"WHITE: Rf1, Kg1, Pf2, Ph2, Pg3, Qf5",
		"BLACK: Kb8, Ne8, Pa7, Pb7, Pc7, Ra5", 
		"PIECE TO MOVE: Rf1"]) == [
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3', 'Qf5'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5'], 'Rf1'], "This is not the right format for our input."

def test_findColorWhite():
	# Find the correct color for the target piece - White
	assert Helpers.findColor([
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3', 'Qf5'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5'], 'Rf1']) == 'w', "Wrong color for the target piece"

def test_findColorBlack():
	# Find the correct color for the target piece - Black
	assert Helpers.findColor([
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3', 'Qf5'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5'], 'Pc7']) == 'b', "Wrong color for the target piece"	

def test_findColorNone():
	# Piece is not on the board
	assert Helpers.findColor([
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3', 'Qf5'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5', ], 'Qh8']) is None, "The target piece not on the board"

def test_validateInput():
	# Invalid by having pieces being in the same square
	assert Helpers.validateInput([
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3', 'Qf5'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5', 'Qf5'], 'Rf1']) is False, "More than one piece in the same square."

def test_movesFunction():
	# Invalid piece input
	assert ChessEngine.movesFunction([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'pg3', 'w') == [], "Invalid letter for the piece. Also, remember to cap."

# Various test cases for drawing pieces, King being in checked and valid moves functions
# 4 different board configurations for testings

def test_drawPieces_board_1():
	assert ChessBoard.drawPieces([
		['Rf1', 'Kg1', 'Pf2', 'Ph2', 'Pg3'], 
		['Kb8', 'Ne8', 'Pa7', 'Pb7', 'Pc7', 'Ra5']]) == [
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], "Board drawn different"

def test_drawPieces_board_2():
	assert ChessBoard.drawPieces([
		['Ra1', 'Kf7', 'Ph7', 'Pb5', 'Nh5', 'Rc4', 'Pc2'], 
		['Pa4', 'Bd3', 'Pg3', 'Ra2', 'Ke1']]) == [
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "wK", "--", "wP"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "wP", "--", "--", "--", "--", "--", "wN"],
	["bP", "--", "wR", "--", "--", "--", "--", "--"],
	["--", "--", "--", "bB", "--", "--", "bP", "--"],
	["bR", "--", "wP", "--", "--", "--", "--", "--"],
	["wR", "--", "--", "--", "bK", "--", "--", "--"]], "Board drawn different"

def test_drawPieces_board_3():
	assert ChessBoard.drawPieces([
		['Qf8', 'Rb7', 'Ba6', 'Pg6', 'Pb5', 'Nb4', 'Kf4', 'Nc1'], 
		['Pc5', 'Kd4', 'Ng4']]) == [
	["--", "--", "--", "--", "--", "wQ", "--", "--"],
	["--", "wR", "--", "--", "--", "--", "--", "--"],
	["wB", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "wP", "bP", "--", "--", "--", "--", "--"],
	["--", "wN", "--", "bK", "--", "wK", "bN", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "wN", "--", "--", "--", "--", "--"]], "Board drawn different"

def test_drawPieces_board_4():
	assert ChessBoard.drawPieces([
		['Pd6', 'Nh6', 'Nb5', 'Bc5', 'Pg5', 'Kb4'], 
		['Qh8', 'Rg6', 'Pd5', 'Pa2', 'Ke3']]) == [
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "bK", "--", "--", "--"],
	["bP", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], "Board drawn different"

def test_inCheck_white():
	assert ChessEngine.inCheck([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'w') is False, "White is not being checked"

def test_inCheck_white2():
	assert ChessEngine.inCheck([
	["--", "--", "--", "--", "--", "wQ", "--", "--"],
	["--", "wR", "--", "--", "--", "--", "--", "--"],
	["wB", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "wP", "bP", "--", "--", "--", "--", "--"],
	["--", "wN", "--", "bK", "--", "wK", "bN", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "wN", "--", "--", "--", "--", "--"]], 'w') is False, "White is not being checked"

def test_inCheck_black():
	assert ChessEngine.inCheck([
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "wK", "--", "wP"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "wP", "--", "--", "--", "--", "--", "wN"],
	["bP", "--", "wR", "--", "--", "--", "--", "--"],
	["--", "--", "--", "bB", "--", "--", "bP", "--"],
	["bR", "--", "wP", "--", "--", "--", "--", "--"],
	["wR", "--", "--", "--", "bK", "--", "--", "--"]], 'b') is True, "Black is being checked"

def test_inCheck_black2():
	assert ChessEngine.inCheck([
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "bK", "--", "--", "--"],
	["bP", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], 'b') is True, "Black is being checked"

def test_getValidMoves_Rook():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Rf1', 'w')) == set(['e1', 'd1', 'c1', 'b1', 'a1']), "Wrong legal moves computed for Rook"

def test_getValidMoves_Rook_inCheck():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "wK", "--", "wP"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "wP", "--", "--", "--", "--", "--", "wN"],
	["bP", "--", "wR", "--", "--", "--", "--", "--"],
	["--", "--", "--", "bB", "--", "--", "bP", "--"],
	["bR", "--", "wP", "--", "--", "--", "--", "--"],
	["wR", "--", "--", "--", "bK", "--", "--", "--"]], 'Ra2', 'b')) == set(['a1']), "Black King is being checked"

def test_getValidMoves_Knight():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Ne8', 'b')) == set(['g7', 'd6', 'f6']), "Wrong legal moves computed for Knight"

def test_getValidMoves_Knight2():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "wQ", "--", "--"],
	["--", "wR", "--", "--", "--", "--", "--", "--"],
	["wB", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "wP", "bP", "--", "--", "--", "--", "--"],
	["--", "wN", "--", "bK", "--", "wK", "bN", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "wN", "--", "--", "--", "--", "--"]], 'Nb4', 'w')) == set(['a2', 'c2', 'd3', 'd5', 'c6']), "Wrong legal moves computed for Knight."

def test_getValidMoves_King():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "wQ", "--", "--"],
	["--", "wR", "--", "--", "--", "--", "--", "--"],
	["wB", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "wP", "bP", "--", "--", "--", "--", "--"],
	["--", "wN", "--", "bK", "--", "wK", "bN", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "wN", "--", "--", "--", "--", "--"]], 'Kf4', 'w')) == set(['f5', 'g5', 'g4', 'g3', 'f3']), "Wrong legal moves computed for King."

def test_getValidMoves_King2():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "bK", "--", "--", "--"],
	["bP", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], 'Ke3','b')) == set(['d3', 'd2', 'e2', 'f3', 'f4', 'e4']), "Black King is being checked."

def test_getValidMoves_King_inCheck():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "wK", "--", "wP"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "wP", "--", "--", "--", "--", "--", "wN"],
	["bP", "--", "wR", "--", "--", "--", "--", "--"],
	["--", "--", "--", "bB", "--", "--", "bP", "--"],
	["bR", "--", "wP", "--", "--", "--", "--", "--"],
	["wR", "--", "--", "--", "bK", "--", "--", "--"]], 'Ke1', 'b')) == set(['d2', 'e2', 'f2']), "Black King is being checked"

def test_getValidMoves_Bishop():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "wQ", "--", "--"],
	["--", "wR", "--", "--", "--", "--", "--", "--"],
	["wB", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "wP", "bP", "--", "--", "--", "--", "--"],
	["--", "wN", "--", "bK", "--", "wK", "bN", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "wN", "--", "--", "--", "--", "--"]], 'Ba6', 'w')) == set([]), "Wrong legal moves computed for Bishop."

def test_getValidMoves_Bishop2():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "bK", "--", "--", "--"],
	["bP", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], 'Bc5','w')) == set(['b6', 'a7', 'd4', 'e3']), "Wrong legal moves computed for Bishop."

def test_getValidMoves_Bishop_inCheck():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "wK", "--", "wP"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "wP", "--", "--", "--", "--", "--", "wN"],
	["bP", "--", "wR", "--", "--", "--", "--", "--"],
	["--", "--", "--", "bB", "--", "--", "bP", "--"],
	["bR", "--", "wP", "--", "--", "--", "--", "--"],
	["wR", "--", "--", "--", "bK", "--", "--", "--"]], 'Bd3', 'b')) == set([]), "Black King is being checked"

def test_getValidMoves_Queen():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bP", "--", "--", "--", "bK", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], 'Qh8','b')) == set(['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h7', 'h6', 'a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7']), "Wrong legal moves computed for Queen."

def test_getValidMoves_Queen_inCheck():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "--", "--", "--", "--", "--", "--", "bQ"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "wP", "--", "--", "bR", "wN"],
	["--", "wN", "wB", "bP", "--", "--", "wP", "--"],
	["--", "wK", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "bK", "--", "--", "--"],
	["bP", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"]], 'Qh8','b')) == set(['d4']), "Black King is being checked."

def test_getValidMoves_whitePawn_2Moves():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Ph2', 'w')) == set(['h3','h4']), "Wrong legal moves computed for White Pawn."

def test_getValidMoves_whitePawn_lefRightCapture():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "bP", "--", "bP"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Pg3', 'w')) == set(['g4','h4', 'f4']), "Wrong legal moves computed for White Pawn."

def test_getValidMoves_whitePawn_edgeBoard():
	# Since the moves should be in an unordered list so I use set() to compare
	# Pawn shoud have been promoted but there is no need for this program
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "wP", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Pf8', 'w')) == set([]), "Wrong legal moves computed for White Pawn."

def test_getValidMoves_blackPawn_2Moves():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Pb7', 'b')) == set(['b5','b6']), "Wrong legal moves computed for Black Pawn."

def test_getValidMoves_blackPawn_leftRightCapture():
	# Since the moves should be in an unordered list so I use set() to compare
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "--", "--", "--", "--", "--", "--"],
	["--", "--", "bP", "--", "--", "--", "--", "--"],
	["bR", "wP", "--", "wP", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "--", "--", "wR", "wK", "--"]], 'Pc6', 'b')) == set(['c5', 'b5', 'd5']), "Wrong legal moves computed for Black Pawn."

def test_getValidMoves_blackPawn_edgeBoard():
	# Since the moves should be in an unordered list so I use set() to compare
	# Pawn shoud have been promoted but there is no need for this program
	assert set(ChessEngine.getValidMoves([
	["--", "bK", "--", "--", "bN", "--", "--", "--"],
	["bP", "bP", "bP", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["bR", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "--", "--"],
	["--", "--", "--", "--", "--", "--", "wP", "--"],
	["--", "--", "--", "--", "--", "wP", "--", "wP"],
	["--", "--", "--", "bP", "--", "wR", "wK", "--"]], 'Pd1', 'b')) == set([]), "Wrong legal moves computed for Black Pawn."
