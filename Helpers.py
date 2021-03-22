
def numToChar(num): # Num to Rank
	map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
	for i in map:
		if map[i] == num:
			return i

def charToNum(char): # Rank to Num
	map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
	for i in map:
		if i == char:
			return map[i]

def numToNum(num): # Reversed Num
	map = {"8": 1, "7": 2, "6": 3, "5": 4, "4": 5, "3": 6, "2": 7, "1": 8}
	for i in map:
		if map[i] == num:
			return i

def getInput(L): # Modify our input
	white, black = [], []
	for i in L:
		if i[:5] == "WHITE":
			w = i[7:].split(',')
			for move in w:
				move_nospace = move.replace(' ','')
				white.append(move_nospace)

		elif i[:5] == "BLACK":
			b = i[7:].split(',')
			for move in b:
				move_nospace = move.replace(' ','')
				black.append(move_nospace)

		else:
			piece = i[15:18]
	input = [white, black, piece]
	return input

def findColor(List): # Find the color of the target piece
	white = List[0]
	black = List[1]

	for piece in white:
		if piece == List[2]:
			return 'w'
	for piece in black:
		if piece == List[2]:
			return 'b'
	return

def validateInput(List): # Make sure the input gives a valid chess board (Correct amount of pieces and they don't overlap in squares)
	white = List[0]
	black = List[1]
	Pos = []
	for L in [white, black]:
		P = {}
		for piece in L:
			if piece[0] not in P:
				P[piece[0]] = 1
			else:
				P[piece[0]] += 1
			if piece[1:] not in Pos:
				Pos.append(piece[1:])
			else:
				return False
		for k in P:
			if k == 'K' and P[k] > 1: return False
			if k == 'Q' and P[k] > 1: return False
			if k == 'R' and P[k] > 2: return False
			if k == 'B' and P[k] > 2: return False
			if k == 'N' and P[k] > 2: return False
			if k == 'P' and P[k] > 8: return False
	return True

def Move(currentBoard, piece, color, curSq, targetSq): # Move a piece to another square
	r = 8-int(curSq[1])
	c = charToNum(curSq[0])-1
	nr = 8-int(targetSq[1])
	nc = charToNum(targetSq[0])-1
	tmp = ''
	currentBoard[r][c] = "--"
	tmp = currentBoard[nr][nc]
	currentBoard[nr][nc] = color + piece[0]
	return tmp
