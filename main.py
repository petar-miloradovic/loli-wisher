from src.menu import *
from src.wish import *
# from src.fight import *
# from src.quests import *

if __name__ == "__main__":
    start = menu_run(bar)
    if start == False:
        exit()
    else:
        igm = menu_inGame(bar)
        match igm:
            case 1: 
                banner = wish_select(bar)
                wish = wish_execute(bar, banner)
            case 2:  
                # fight
                pass
            case 3:
                # quests
                pass