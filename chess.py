# chessBoard = [[1] * 8 for i in range(8)]
castle = "C"
bishop = "B"
horse = "H"
queen = "Q"
pawn = "P"
king = "K"
empty= " "

chessBoard = [
    [castle, horse, bishop, queen, king, bishop, horse, castle],
    [pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn],
    [castle, horse, bishop, queen, king, bishop, horse, castle]]
def printBoard(c):
    print("  ---------------------------------")
    for i in range(len(c)):
        print(str(i+1)+" |",end="")
        for j in range(len(c[i])):
            print(" "+c[i][j]+" ",end="|")
        print()
        print("  ---------------------------------")
    print("    a   b   c   d    e   f   g   h")

printBoard(chessBoard)
chess_map_from_alpha_to_index = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8
}

chess_map_from_index_to_alpha = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h"
}

# knight
def knight(location):
    a = location[0]
    b = location[1]
    options_c1 = [1,-1]
    options_r1 = [2,-2]
    options_r2 = [1,-1]
    options_c2 = [2,-2]
    x = 0
    y = 0
    options = []
    for i in range(2):
        x = chess_map_from_index_to_alpha[chess_map_from_alpha_to_index[a]+options_c1[i]]
        for j in range(2):
            y = int(b)+options_r1[j]
            options.append(x+str(y))
    for i in range(2):
        x = chess_map_from_index_to_alpha[chess_map_from_alpha_to_index[a]+options_c2[i]]
        for j in range(2):
            y = int(b)+options_r2[j]
            options.append(x+str(y))
    print(options)
    return options
knight("e4")
#testing


# rook
def rook(location):
    a = location[0]
    b = location[1]
    options = []
    for i in range(1,9):
        if location != (a+str(i)):
            options.append(a+str(i))
    for j in range(1,9):
        x = chess_map_from_index_to_alpha[j]+b
        if x != location:
            options.append(x)
    print(options)
    return options
rook("e4")
#testing

# bishop
def bishop(location):
    a = location[0]
    b = location[1]
    options = []
    for i in range(1,9):
        c = chess_map_from_alpha_to_index[a]-i
        s = (int(b) + c)
        if s > 0 and s < 9:
            options.append(chess_map_from_index_to_alpha[i]+str(s))
        s = (int(b) - c)
        if s > 0 and s < 9:
            options.append(chess_map_from_index_to_alpha[i]+str(s))
    i=0
    while i in range(len(options)):
        if options[i]==location:
            options.pop(i)
        else:
            i+=1
        if(i>=len(options)):
            break
    print(options)
    return options
bishop("e4")
#testing

# queen
def queen(location):
    options = []
    options.append(rook(location))
    options.append(bishop(location))
    return options
# pawn
def pawn(location):
    options = []
    a = location[0]
    b = location[1]
    if(b==7):
        options.append(a+str(int(b)-2))
    options.append(a+str(int(b)-1))
    options.append(chess_map_from_index_to_alpha[chess_map_from_alpha_to_index[a]+1]+str(int(b)-1))
    options.append(chess_map_from_index_to_alpha[chess_map_from_alpha_to_index[a]-1]+str(int(b)-1))
    return options

def playGame():
    while True:
        player1()
        player2()
    return True

def player1():
    print("player 1: ")

    return True

def player2():
    print("player 2: ")

    return True

def gameOver():
    checkmate = True
    return checkmate