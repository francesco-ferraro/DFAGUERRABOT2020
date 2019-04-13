import map
import secrets
from time import sleep

Z_DIST = 1

LOCATIONS = [
    [[75, 60, 0], [89, 184, 226]],
    [[112, 60, 0], [89, 184, 226]],
    [[75, 90, 0], [239, 211, 111]],
    [[112, 90, 0], [178, 107, 152]],
    [[161, 60, 0], [155, 111, 75]],
    [[198, 60, 0], [250, 4, 185]],
    [[161, 90, 0], [175, 161, 70]],
    [[198, 90, 0], [119, 46, 255]],
    [[247, 60, 0], [215, 133, 8]],
    [[285, 60, 0], [161, 112, 0]],
    [[247, 90, 0], [230, 7, 145]],
    [[285, 90, 0], [208, 236, 11]],
    [[90, 36, 0], [132, 222, 3]],
    [[150, 36, 0], [28, 79, 50]],
    [[210, 36, 0], [23, 127, 80]],
    [[270, 36, 0], [241, 234, 99]],
    [[75, 60, 1], [148, 185, 10]],
    [[112, 60, 1], [72, 128, 54]],
    [[75, 90, 1], [76, 21, 56]],
    [[112, 90, 1], [33, 64, 72]],
    [[161, 60, 1], [83, 169, 15]],
    [[198, 60, 1], [46, 225, 175]],
    [[161, 90, 1], [127, 81, 254]],
    [[198, 90, 1], [78, 31, 127]],
    [[247, 60, 1], [34, 164, 248]],
    [[285, 60, 1], [31, 15, 180]],
    [[247, 90, 1], [230, 14, 149]],
    [[285, 90, 1], [249, 246, 240]],
    [[90, 36, 1], [248, 59, 143]],
    [[150, 36, 1], [202, 164, 124]],
    [[210, 36, 1], [25, 45, 6]],
    [[270, 36, 1], [40, 214, 117]],
    [[75, 60, 2], [77, 188, 249]],
    [[112, 60, 2], [254, 105, 72]],
    [[75, 90, 2], [113, 25, 64]],
    [[112, 90, 2], [66, 104, 143]],
    [[161, 60, 2], [140, 120, 236]],
    [[198, 60, 2], [73, 123, 94]],
    [[161, 90, 2], [254, 167, 152]],
    [[198, 90, 2], [104, 3, 99]],
    [[247, 60, 2], [27, 24, 241]],
    [[285, 60, 2], [47, 16, 9]],
    [[247, 90, 2], [34, 73, 27]],
    [[285, 90, 2], [39, 254, 120]],
    [[90, 36, 2], [2, 148, 8]],
    [[150, 36, 2], [120, 254, 26]],
    [[210, 36, 2], [234, 74, 131]],
    [[270, 36, 2], [201, 255, 108]]
]

def owner(players, location):
    '''
    Returns the owner of the given location
    '''
    for i in range(len(players)):
        if location in players[i]:
            return i

def squared_distance(location1, location2):
    return (location1[0][0]-location2[0][0])**2 + \
           (location1[0][1]-location2[0][1])**2 + \
           (Z_DIST*(location1[0][2]-location2[0][2]))**2
    
def nearest(players, location):
    '''
    Returns a list of the locations nearest to the given one, based on minimum
    'squared_distance', excluding locations already occupied by the owner.
    Returns None if the owner occupies all locations.
    '''
    
    current_owner = owner(players, location)
    excluded_players = players[current_owner]
    
    nearest = None
    min_distance = float("inf")  
    
    for i in range(len(LOCATIONS)):
        if i in excluded_players: continue
        distance = squared_distance(LOCATIONS[current_owner], LOCATIONS[i])
        if distance == min_distance:
            nearest.append(i)
        if distance < min_distance:
            min_distance = distance
            nearest = [i]
            
    return nearest

def write_players(players, file):
    '''
    Writes 'state' in a file, overwriting
    '''
    
    with open(file, "w") as f:
        for player in players:
            for location in player:
                f.write(str(location) + " ")
            f.write("\n")
            
def read_players(file):
    '''
    Returns the previously saved state
    '''
    
    players = []
     
    with open(file, "r") as f:
        for line in f:
            players.append([int(i) for i in line.split()])
            
    return players
    
def generate_color_list(players):
    '''
    Returns the color list ready to be fed into show_map
    '''
    
    colors = []
    
    for i in range(len(LOCATIONS)):
        colors.append(LOCATIONS[owner(i)][1])
        
    return colors


# Modalità:
# 0 - fa una partita completa da capo, senza grafica
# 1 - fa una partita completa dallo stato salvato, senza grafica
# 2 - legge il file salvato, fa una mossa, mostra la mappa
# 3 - legge il file salvato, fa una mossa, mostra la mappa, salva il file

mode = 2

if mode == 0 or mode==1:
    if mode == 0:
        players = read_players("vanilla_state.txt")
    if mode == 1:    
        players = read_players("saved_state.txt")
        
    while True:
        random_location = secrets.randbelow(len(LOCATIONS))
        near_locations = nearest(players, random_location)
        
        if near_locations is not None:
            target_location = secrets.choice(near_locations)
            
            winner = owner(players, random_location)
            loser = owner(players, target_location)

            players[loser].remove(target_location)
            players[winner].append(target_location)
            
            print(str(winner) + " conquista " + str(loser) + \
                  " in " + str(target_location))
        else:
            print(winner)
            break
elif mode == 2:
    pass
elif mode == 3:
    pass

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