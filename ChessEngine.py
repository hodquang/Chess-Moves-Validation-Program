import Helpers

def getValidMoves(currentBoard, piece, color): # Determine all the valid moves for our piece
	moves = movesFunction(currentBoard, piece, color)
	counter = 0
	validMoves = []
	while counter < len(moves):
		tmp = Helpers.Move(currentBoard, piece, color, piece[1:3],moves[counter])
		if inCheck(currentBoard, color) is False:
			validMoves.append(moves[counter])
		Helpers.Move(currentBoard, piece, color, moves[counter],piece[1:3])
		currentBoard[8-int(moves[counter][1])][Helpers.charToNum(moves[counter][0])-1] = tmp
		counter += 1
	return validMoves

def inCheck(currentBoard, color): # Determine if the current color is being checked
	enemyColor = "b" if color == 'w' else "w"
	enemyMoves = getAllPossibleMoves(currentBoard, enemyColor)
	if locateKing(currentBoard, color) in enemyMoves:
		return True
	else:
		return False

def locateKing(currentBoard, color): # Find the King location
	coord = ''
	for r in range(8):
		for c in range(8):
			piece = currentBoard[r][c]
			if piece[0] == color and piece[1] == 'K':
				coord = Helpers.numToChar(c+1) + Helpers.numToNum(r+1)
	return coord

def getAllPossibleMoves(currentBoard, color): # Compute all possible moves for one color
	moves = []
	for r in range(8):
		for c in range(8):
			piece = currentBoard[r][c]
			if piece != "--" and piece[0] == color:
				coord = piece[1]+Helpers.numToChar(c+1)+str(Helpers.numToNum(r+1))
				moves = moves + movesFunction(currentBoard, coord, piece[0])
	return moves

def movesFunction(currentBoard, piece, color): # Check to see the what piece is our targeted piece
	if piece[0] == 'P':
		return getPawnMoves(currentBoard, piece, color)
	elif piece[0] == 'R':
		return getRookMoves(currentBoard, piece, color)
	elif piece[0] == 'N':
		return getKnightMoves(currentBoard, piece, color)
	elif piece[0] == 'B':
		return getBishopMoves(currentBoard, piece, color)
	elif piece[0] == 'Q':
		return getQueenMoves(currentBoard, piece, color)
	elif piece[0] == 'K':
		return getKingMoves(currentBoard, piece, color)
	else:
		return []

def getPawnMoves(currentBoard, piece, color):
	moves = []
	r = 8-int(piece[2])
	c = Helpers.charToNum(piece[1])-1
	if color == 'w': # white moves
		if r == 0: return moves
		if currentBoard[r-1][c] == "--":
			moves.append(Helpers.numToChar(c+1) + Helpers.numToNum(r))
			if r == 6 and currentBoard[r-2][c] == "--":
				moves.append(Helpers.numToChar(c+1) + Helpers.numToNum(r-1))
		# captures
		if c-1 >= 0: # left
			if currentBoard[r-1][c-1][0] == 'b':
				moves.append(Helpers.numToChar(c) + Helpers.numToNum(r))
		if c+1 <= 7: # right
			if currentBoard[r-1][c+1][0] == 'b':
				moves.append(Helpers.numToChar(c+2) + Helpers.numToNum(r))
	elif color == 'b': # black moves
		if r == 7: return moves
		if currentBoard[r+1][c] == "--":
			moves.append(Helpers.numToChar(c+1) + Helpers.numToNum(r+2))
			if r == 1 and currentBoard[r+2][c] == "--":
				moves.append(Helpers.numToChar(c+1) + Helpers.numToNum(r+3))
		# captures
		if c-1 >= 0: # left
			if currentBoard[r+1][c-1][0] == 'w':
				moves.append(Helpers.numToChar(c) + Helpers.numToNum(r+2))
		if c+1 <= 7: # right
			if currentBoard[r+1][c+1][0] == 'w':
				moves.append(Helpers.numToChar(c+2) + Helpers.numToNum(r+2))
	return moves


def getRookMoves(currentBoard, piece, color):
	moves = []
	directions = ((-1,0), (0,-1), (1,0), (0,1)) # verical and horizontal
	enemyColor = "b" if color == 'w' else "w"
	r = 8-int(piece[2])
	c = Helpers.charToNum(piece[1])-1
	for d in directions:
		for i in range(1,8):
			endRow = r + d[0]*i
			endCol = c + d[1]*i
			if 0 <= endRow < 8 and 0 <= endCol < 8:
				endPiece = currentBoard[endRow][endCol]
				if endPiece == "--":
					moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
				elif endPiece[0] == enemyColor:
					moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
					break
				else:
					break
			else:
				break
	return moves


def getKnightMoves(currentBoard, piece, color):
	moves = []
	r = 8-int(piece[2])
	c = Helpers.charToNum(piece[1])-1
	knightMoves = ((-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)) # L-shape
	allyColor = "w" if color == 'w' else "b"
	for m in knightMoves:
		endRow = r + m[0]
		endCol = c + m[1]
		if 0 <= endRow < 8 and 0 <= endCol < 8:
			endPiece = currentBoard[endRow][endCol]
			if endPiece[0] != allyColor:
				moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
	return moves


def getBishopMoves(currentBoard, piece, color):
	moves = []
	r = 8-int(piece[2])
	c = Helpers.charToNum(piece[1])-1
	directions = ((-1,-1), (-1,1), (1,-1),(1,1)) # Diagonal
	enemyColor = "b" if color == 'w' else "w"
	for d in directions:
		for i in range(1,8):
			endRow = r + d[0] * i
			endCol = c + d[1] * i
			if 0 <= endRow < 8 and 0 <= endCol < 8:
				endPiece = currentBoard[endRow][endCol]
				if endPiece == "--":
					moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
				elif endPiece[0] == enemyColor:
					moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
					break
				else:
					break
			else:
				break
	return moves

def getQueenMoves(currentBoard, piece, color):
	# Rook and Bishop combine
	return getRookMoves(currentBoard, piece, color) + getBishopMoves(currentBoard, piece, color)

def getKingMoves(currentBoard, piece, color):
	moves = []
	r = 8-int(piece[2])
	c = Helpers.charToNum(piece[1])-1

	kingMoves = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)) # Squares around it
	allyColor = "w" if color == 'w' else "b"
	for i in range(8):
		endRow = r + kingMoves[i][0]
		endCol = c + kingMoves[i][1]
		if 0 <= endRow < 8 and 0 <= endCol < 8:
			endPiece = currentBoard[endRow][endCol]
			if endPiece[0] != allyColor:
				moves.append(Helpers.numToChar(endCol+1)+Helpers.numToNum(endRow+1))
	return moves
