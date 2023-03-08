import json

def pity(banner):
    '''
    Base chanche is % value
    pity can be maximum 90
    at 90 you have 100% 5 star and reset pity value(0) in fj
    '''
    with open('banners/'+banner+'.json') as f:
        fj = json.load(f)
        pity = fj['pity']
        base_chance = fj['base_chance']
        star5_chance = base_chance + pity
        pity = 
        if star5_chance == 90:
            return True
        else: 
            return False