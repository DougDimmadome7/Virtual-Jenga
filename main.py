
import jenga
from bots import RandomBot
 
def input_user() -> int:
    """
    Accepts user input for what piece to move, returns two integers,
    one for which layer to pick, the next for which index to pick.
    """
    height = int(input("Which layer? "))
    index = int(input("Which index? "))
 
    return (height, index)
 
def player_turn(tower):
    height, index = input_user()
    tower.move_piece(height, index)
    tower.display()
    if tower.will_fall():
        return False
    else:
        return True
 
def game_loop(players: int, bots: list, height = 15):
    t1 = jenga.Tower(height)
    game_going = True
    while game_going:
        if player_turn(t1):
            for bot in bots:
                if not bot.turn(t1):
                    print("You Win")
                    game_going = False
                    break
        else:
            print("You Lose")
            game_going = False
 
    
        
 
game_loop(2, [RandomBot()], 17)
 
 

