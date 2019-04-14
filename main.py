import map
import secrets
from time import sleep

# Modalità:
# 0 - fa una partita completa da capo, senza grafica
# 1 - fa una partita completa dallo stato salvato, senza grafica
# 2 - legge il file salvato, fa una mossa, mostra la mappa
# 3 - legge il file salvato, fa una mossa, mostra la mappa, salva file+screen
# 4 - genera istogramma delle vittorie da capo
# 5 - legge il file salvato, genera istogramma delle vittorie
# 6 - istogramma lunghezza partite da capo
# 7 - istogramma lunghezza partite da stato salvato
# 8 - testing
mode = 3

GAME_NUMBER = 5000

Z_DIST = 90

LOCATIONS = [
    [[75,  60, 0], [138, 45,  216]],
    [[112, 60, 0], [176, 3,   127]],
    [[75,  90, 0], [112, 77,  110]],
    [[112, 90, 0], [237, 36,  167]],
    [[161, 60, 0], [35,  0,   209]],
    [[198, 60, 0], [75,  97,  144]],
    [[161, 90, 0], [17,  61,  27 ]],
    [[198, 90, 0], [223, 68,  15 ]],
    [[247, 60, 0], [146, 59,  168]],
    [[285, 60, 0], [223, 130, 138]],
    [[247, 90, 0], [48,  84,  7  ]],
    [[285, 90, 0], [159, 9,   242]],
    [[90,  36, 0], [186, 111, 64 ]],
    [[150, 36, 0], [226, 224, 17 ]],
    [[210, 36, 0], [28,  175, 91 ]],
    [[270, 36, 0], [160, 200, 253]],
    [[75,  60, 1], [151, 40,  244]],
    [[112, 60, 1], [218, 245, 252]],
    [[75,  90, 1], [58,  74,  137]],
    [[112, 90, 1], [90,  223, 250]],
    [[161, 60, 1], [226, 80,  1  ]],
    [[198, 60, 1], [56,  135, 69 ]],
    [[161, 90, 1], [163, 118, 36 ]],
    [[198, 90, 1], [154, 115, 127]],
    [[247, 60, 1], [160, 101, 222]],
    [[285, 60, 1], [245, 155, 125]],
    [[247, 90, 1], [177, 202, 187]],
    [[285, 90, 1], [230, 247, 246]],
    [[90,  36, 1], [86,  255, 55 ]],
    [[150, 36, 1], [35,  6,   153]],
    [[210, 36, 1], [89,  26,  125]],
    [[270, 36, 1], [129, 210, 128]],
    [[75,  60, 2], [9,   149, 11 ]],
    [[112, 60, 2], [51,  88,  152]],
    [[75,  90, 2], [252, 216, 11 ]],
    [[112, 90, 2], [244, 121, 131]],
    [[161, 60, 2], [250, 141, 53 ]],
    [[198, 60, 2], [224, 66,  119]],
    [[161, 90, 2], [93,  77,  194]],
    [[198, 90, 2], [136, 8,   77 ]],
    [[247, 60, 2], [183, 247, 122]],
    [[285, 60, 2], [30,  19,  118]],
    [[247, 90, 2], [40,  185, 126]],
    [[285, 90, 2], [100, 81,  90 ]],
    [[90,  36, 2], [23,  11,  186]],
    [[150, 36, 2], [56,  160, 90 ]],
    [[210, 36, 2], [85,  40,  20 ]],
    [[270, 36, 2], [131, 176, 168]]
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
        colors.append(LOCATIONS[owner(players,i)][1])
        
    return colors


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
            
elif mode == 2 or mode == 3:
    players = read_players("saved_state.txt")
    initial_colors = generate_color_list(players)
    
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
        
        new_colors = generate_color_list(players)
        
        
        if mode == 2:
            map.replot(initial_colors, new_colors, 0)
        elif mode == 3:
            map.replot(initial_colors, new_colors, 1)
            write_players(players, "saved_state.txt")
    else:
        print(winner)

elif mode == 4 or mode == 5:    
    winners = [0] * len(LOCATIONS)
    
    for i in range(GAME_NUMBER):
        if mode == 4:
            players = read_players("vanilla_state.txt")
        if mode == 5:
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
            else:
                winners[winner] += 1
                break
                
    print(winners)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    n = ax.bar(range(len(LOCATIONS)), winners, tick_label=range(len(LOCATIONS)))
    plt.title("z= " + str(Z_DIST) + " N=" + str(GAME_NUMBER))
    plt.show()
    
elif mode == 6 or mode == 7:
    game_lenghts = []
    
    for i in range(GAME_NUMBER):
        if mode == 6:
            players = read_players("vanilla_state.txt")
        if mode == 7:
            players = read_players("saved_state.txt")
        
        game_lenght = 0
        
        while True:
            game_lenght += 1
            random_location = secrets.randbelow(len(LOCATIONS))
            near_locations = nearest(players, random_location)
    
            if near_locations is not None:
                target_location = secrets.choice(near_locations)
        
                winner = owner(players, random_location)
                loser = owner(players, target_location)

                players[loser].remove(target_location)
                players[winner].append(target_location)
            else:
                break
        game_lenghts.append(game_lenght)
        
    print(game_lenghts)
    
    import matplotlib.pyplot as plt

    num_bins = 50
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(game_lenghts, num_bins, density=1)
    plt.title("z=" + str(Z_DIST) + " N=" + str(GAME_NUMBER))
    plt.show()