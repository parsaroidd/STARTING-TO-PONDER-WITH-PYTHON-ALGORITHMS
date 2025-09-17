choice = input("give me the place of ur knight exactly like this: (width, height) \n e.g: (4,3): ")

first_moves, real_moves = [], [] 

def first_move(x, y):

    possible_moves = { #__ the top left is (1,1) and the numbers increases if we go <right> or <down>_____#
        'up-right': (x - 2, y + 1),
        'up-left': (x - 2, y - 1),
        'down-right': (x + 2, y + 1),
        'down-left': (x + 2, y -1 ),
        'left-up': (x - 1, y - 2),
        'left-down': (x + 1, y - 2),
        'right-up': (x - 1, y + 2),
        'right-down': (x + 1, y + 2)
    }

    for move in possible_moves:
        if 0 < possible_moves[move][0] <= 8 and 0 < possible_moves[move][1] <= 8:
            first_moves.append(possible_moves[move])


first_move(x = int(choice[1]), y = int(choice[3])) #now i know all the possible moves at the first, but no idea where to go from here...

def play(x):
    new_move = first_moves[x]

    for i in range(20):
        init_length = len(first_moves)

        if init_length < 1:
            print("dude sumn is worng")
            break 

        else:
            first_moves.clear()
            first_move(new_move[0], new_move[1])
            if len(first_moves) > 0:
                real_moves.append(new_move)
                play(x)

            else:
                play(x + 1)

play(0)
print(real_moves)

#my idea is to use one element of first_moves list and then iterate it over and over...
#def play():
#    init_length = len(first_moves)
#    first_move(x = first_moves[0][0], y = first_moves[0][1])
#    if len(first_moves) > init_length:
#        real_moves.append()

#def test(): i wanted to see if i can store the length before clearing the list or not....
#    length = len(first_moves)
#    first_moves.clear()
#    print(length)

