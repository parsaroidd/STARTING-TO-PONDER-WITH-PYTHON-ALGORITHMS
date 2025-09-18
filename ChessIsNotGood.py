choice = 33

ok, board, fake= [], [], []

def fill(num):
    possible = {
        'si_x': num - 6,
        'te_n': num - 10 ,
        'fiftee_n': num - 15,
        'seventee_n': num - 17 ,
        'six': num + 6 ,
        'ten':num + 10 ,
        'fifteen': num + 15 ,
        'seventeen': num + 17 
        }
    
    for i in possible:
        if 0 < possible[i] < 65:
            ok.append(possible[i])

fill(choice)

#def solve():
#    for i in range(len(ok)):
#        fill(ok[i])

def solve():

    if len(board) == 63:
        pass 
    else:
        for i in range(len(ok)):
            init = len(ok)
            fake.append(ok[i])
            fill(fake[0])
            if len(ok) > init:
                solve()
                break 
            else: continue

solve()
            
