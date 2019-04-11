import map
from secrets import randbelow
from time import sleep

Z_DIST = 1

LOCATIONS = [
    [0, [75, 60, 0], [89, 184, 226]],
    [1, [112, 60, 0], [89, 184, 226]],
    [2, [75, 90, 0], [239, 211, 111]],
    [3, [112, 90, 0], [178, 107, 152]],
    [4, [161, 60, 0], [155, 111, 75]],
    [5, [198, 60, 0], [250, 4, 185]],
    [6, [161, 90, 0], [175, 161, 70]],
    [7, [198, 90, 0], [119, 46, 255]],
    [8, [247, 60, 0], [215, 133, 8]],
    [9, [285, 60, 0], [161, 112, 0]],
    [10, [247, 90, 0], [230, 7, 145]],
    [11, [285, 90, 0], [208, 236, 11]],
    [12, [90, 36, 0], [132, 222, 3]],
    [13, [150, 36, 0], [28, 79, 50]],
    [14, [210, 36, 0], [23, 127, 80]],
    [15, [270, 36, 0], [241, 234, 99]],
    [16, [75, 60, 1], [148, 185, 10]],
    [17, [112, 60, 1], [72, 128, 54]],
    [18, [75, 90, 1], [76, 21, 56]],
    [19, [112, 90, 1], [33, 64, 72]],
    [20, [161, 60, 1], [83, 169, 15]],
    [21, [198, 60, 1], [46, 225, 175]],
    [22, [161, 90, 1], [127, 81, 254]],
    [23, [198, 90, 1], [78, 31, 127]],
    [24, [247, 60, 1], [34, 164, 248]],
    [25, [285, 60, 1], [31, 15, 180]],
    [26, [247, 90, 1], [230, 14, 149]],
    [27, [285, 90, 1], [249, 246, 240]],
    [28, [90, 36, 1], [248, 59, 143]],
    [29, [150, 36, 1], [202, 164, 124]],
    [30, [210, 36, 1], [25, 45, 6]],
    [31, [270, 36, 1], [40, 214, 117]],
    [32, [75, 60, 2], [77, 188, 249]],
    [33, [112, 60, 2], [254, 105, 72]],
    [34, [75, 90, 2], [113, 25, 64]],
    [35, [112, 90, 2], [66, 104, 143]],
    [36, [161, 60, 2], [140, 120, 236]],
    [37, [198, 60, 2], [73, 123, 94]],
    [38, [161, 90, 2], [254, 167, 152]],
    [39, [198, 90, 2], [104, 3, 99]],
    [40, [247, 60, 2], [27, 24, 241]],
    [41, [285, 60, 2], [47, 16, 9]],
    [42, [247, 90, 2], [34, 73, 27]],
    [43, [285, 90, 2], [39, 254, 120]],
    [44, [90, 36, 2], [2, 148, 8]],
    [45, [150, 36, 2], [120, 254, 26]],
    [46, [210, 36, 2], [234, 74, 131]],
    [47, [270, 36, 2], [201, 255, 108]]
]

def squared_distance(location1, location2):
    return (location1[1][0]-location2[1][0])**2 + \
           (location1[1][1]-location2[1][1])**2 + \
           (Z_DIST*(location1[1][2]-location2[1][2]))**2
    
def nearest(location):
    '''
    Returns the location nearest to the given one, based on minimum
    'squared_distance', excluding locations already occupied by the owner.
    Returns None if the owner occupies all locations.
        '''
    
    current_owner = owner(location)
    excluded_players = players[current_owner]
    
    nearest = None
    min_distance = float("inf")  
    
    for i in range(len(LOCATIONS)):
        if i in excluded_players: continue
        distance = squared_distance(LOCATIONS[current_owner], LOCATIONS[i])
        if distance < min_distance:
            min_distance = distance
            nearest = i
            
    return nearest

def owner(location):
    '''
    Returns the owner of the given location
    '''
    for i in range(len(players)):
        if location in players[i]:
            return i

# Game inizialization
players = []

# Vanilla start: every player owns itself
for i in range(len(LOCATIONS)):
    players.append([i])
    
(color, vettoreperfra) = map.initialplot()   

while True:
    random_location = randbelow(len(LOCATIONS))
    target_location = nearest(random_location)

    if target_location is not None:    
        winner = owner(random_location)
        loser = owner(target_location)

        players[loser].remove(target_location)
        players[winner].append(target_location)
   
        colorup = map.updatecolor(target_location, winner, color)
        (color, vettoreperfradopolaguerra) = map.replot(colorup)
        
        print(str(winner) + " conquista " + str(loser) + " in " + str(target_location))
    else:
        print(winner)
        break

# '''
# inizializza la mappa: genera i colori degli uffici a random
# ritorna i colori degli uffici [[RGB1_uff1, RGB2_uff1, RGB3_uff1]...[RGB1_uff48, RGB2_uff48, RGB3_uff48]]
# '''
# (color, vettoreperfra) = map.initialplot()
# '''
# updatecolor(ufficio sconfitto, ufficio vincitore, color)
# ritorna il vettore dei colori aggiornato dopo la battaglia e il vettore che ti serve
# '''
# colorup = map.updatecolor(1, 0, color)
# (color, vettoreperfradopolaguerra) = map.replot(colorup)
#
# print(vettoreperfradopolaguerra)