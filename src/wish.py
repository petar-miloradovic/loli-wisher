import os
from pity import pity

bar = "-"*100

def wish_select(bar):
    '''
    this function shows you all the gems
    then it shows you all the wish banners list
    and asks you to chose one from them
    '''
    print(bar)
    # get banners array
    banners = list()
    for path in os.listdir('banners/'):
        if os.path.isfile(os.path.join('banners/', path)):
            banners.append(path.removesuffix('.json')) # banner name without .json
    print("now select the banner you wanna pull from these:")
    # show all the banners and ask which one
    for i in len(banners):
        print(banners[i])
    banner = input("type here --> ")
    while banner in banners == False:
        print("you entered an invalid answer, plz write again")
        banner = input("type here --> ")
    print(bar)
    return banner

def wish_execute(bar, banner):
    '''
    this function shows you all the gems
    then asks you how many pulls you wanna do
    it does 1 or 10 pull(according to the times variable)
    '''
    print(bar)
    # select from multi or single wish
    print("now tell us how many times do you want to run the wish",
        "it can be 1 for 160 gems",
        "or it can be 10 for 1600 gems")
        # "or it can be 100 for 16000 gems")
    times = int(input("type here -->"))
    while times != 1 and times != 10: # and times != 100
        print("you entered an invalid answer, plz write again")
        banner = input("type here --> ")

    # pull
    print(times+"x pull on", banner+":")
    for i in range(times):
        # execute the pity (true/false)
        '''
        add c and a bit of gems, 
        if c = 6 it gives more gems, 
        if prevuous c < 0 it gives no gems
        when pity(in script) goes true, it goes 0(resets) on wish_name.json
        '''
        pass
