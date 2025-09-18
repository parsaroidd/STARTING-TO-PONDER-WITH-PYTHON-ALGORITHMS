choice = "[4,3]" #input("give me the place of ur knight exactly like this: (width, height) \n e.g: (4,3): ")

first_moves, real_moves, fake_moves = [], [] , []

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

first_move(int(choice[1]), int(choice[3]))

print(first_moves) #if i just make this a loop the program will work...

def play2():
    for i in first_moves:
        first_move(list(first_moves[i])[0], list(first_moves[i])[1])

def play1():
    
    for move in range(len(first_moves)):

        init_length = len(first_moves)

        fake_moves.append(first_moves[move])

        first_move(first_moves[move][0], first_moves[move][1])

        if len(first_moves) == init_length: #gotta pop it from the first moves....

            first_moves.pop(first_moves[move])
    
def play():

    psudo = []
    

    for move in range(len(first_moves)):
        psudo.append(first_moves[move])
        first_move(psudo[0][0], psudo[0][1])

play2()
print(first_moves)


