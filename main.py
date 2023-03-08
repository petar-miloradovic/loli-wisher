from src.menu import *
from src.wish import *
from src.fight import *
from src.quests import *

if __name__ == "__main__":
    start = menu_run()
    if start == False:
        exit()
    else:
        igm = menu_inGame()
        match igm:
            case 1: 
                wish = wish_select()
                wish = wish_execute()
            case 2:  
                # fight
                pass
            case 3:
                # quests
                pass