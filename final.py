say, mess_with, mumble = print, input, int  

User_stuff = mumble(mess_with("Where i gotta start champ? "))

engine = [] 

def fill(knight):
        What_can_you_do = [
        knight - 6, knight - 10, knight - 15, knight - 17,
        knight + 6, knight + 10, knight + 15, knight + 17
    ]
        return [stuff for stuff in What_can_you_do if 0 < stuff < 65]

def Engine(move, went_there):
        
        if len(went_there) == 64:
                return went_there 
        
        juice = fill(move)
        for water in juice:
                if water not in went_there:
                        final = Engine(water, went_there + [water])
                        if final:
                                return final 
                        
say(Engine(User_stuff, [User_stuff]))

            

