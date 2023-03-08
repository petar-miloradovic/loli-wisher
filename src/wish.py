import os

bar = "-"*100

def wish_select(bar):
    '''
    this function shows you the wish banner list
    after you select the wish, you can choice for a single(x1) or a multi(x10)
    '''
    print(bar)
    banners = list()
    for path in os.listdir('banners/'):
        if os.path.isfile(os.path.join('banners/', path)):
            banners.append(path.removesuffix('.json'))
    print("now select the banner you wanna pull from these:")
    for i in len(banners):
        print(banners[i])
    read = input()

def wish_execute(bar, times, banner):
    '''
    this function gets times and the banner name from wish select
    it does 1 or 10 pull(according to the times variable)
    '''
    for i in range(times):
        pass 
