bar = "-"*100

def menu_run(bar):
    '''
    this menu shows two different choices:
    the first one is to start the game,
    and the second one is to kill the process(close the game).
    it returns true or false
    '''
    print(bar)
    print("Main menu:",
        "write \"start\" to start the game",
        "write \"close\" to close the game" 
        )
    choice = input("type here --> ")
    while choice != "start" and choice != "close":
        print("wrong input,",
            "try again following the previous suggestions")
        choice = input("type here --> ")
    print(bar)
    match choice:
        case "start": return True 
        case "close": return False

def menu_inGame(bar):
    '''
    this menu shows three different options:
    the first one opens the wish menu,
    the second one the fight menu,
    and the third one the quests menu.
    it returns 1 for wish, 2 for fight and 3 for quests
    '''
    print(bar)
    print("In game menu:",
        "write \"wish\" to enter the wish menu",
        "write \"fight\" to enter the fight menu",
        "write \"quests\" to open the quests menu"
        )
    choice = input("type here --> ")
    while choice != "wish" and choice != "fight" and choice !="quests":
        print("wrong input,",
            "try again following the previous suggestions")
        choice = input("type here --> ")
    print(bar)
    match choice:
        case "wish": return 1
        case "fight": return 2
        case "quests": return 3