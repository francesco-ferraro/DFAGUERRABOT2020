import map
import secrets

# Modalità:
# 0 - fa una partita completa da capo, senza grafica
# 1 - fa una partita completa dallo stato salvato, senza grafica
# 2 - legge il file salvato, fa una mossa, mostra la mappa
# 3 - legge il file salvato, fa una mossa, mostra la mappa, salva file + screen
# 4 - istogramma vincitori da capo
# 5 - istogramma vincitori da stato salvato
# 6 - istogramma lunghezza partite da capo
# 7 - istogramma lunghezza partite da stato salvato
# 9 - schermata iniziale + screen
# 10 - schermata attuale + screen
# 11 - testing

mode = 9

GAME_NUMBER = 5000

Z_DIST = 30

NAMES = [
    'Pironi-Cesaro', 
    'Salasnich',
    'Baiesi',
    'Trovato',
    'Agarfa',
    'Enrico',
    'Stanco',
    'Lunardon',
    'Roberto',
    'Mistura',
    'Lacaprara',
    'Mazzocco',
    'Sada',
    'Carnera',
    'Baldassarri',
    'Vittadini',
    'Patelli',
    'Vittone',
    'Monti',
    'Marastoni',
    'Marchetti',
    'Matone',
    'Uomo Civis',
    'Lechner',
    'Fassò',
    'Benettin',
    'Matarrese',
    'Carmela',
    'Zanetti',
    "Dall'Agata",
    'Bottaccin',
    '????',
    'Mengoni',
    'Stella',
    'Orlandini',
    'Maritan',
    'Zwirner',
    'Feruglio',
    'Fortunato',
    'Lucchesi',
    'Borghesani',
    'Pierno',
    'Zendri',
    'Giusto',
    'Martucci',
    'Peruzzi',
    'Bastieri']

LOCATIONS = [
    [[75,  60, 0], [155, 202,  47]],
    [[112, 60, 0], [175, 237, 255]],
    [[75,  90, 0], [ 17,  53, 179]],
    [[112, 90, 0], [105,  58, 142]],
    [[161, 60, 0], [ 54,  98, 169]],
    [[198, 60, 0], [226,  45, 255]],
    [[161, 90, 0], [249, 139, 224]],
    [[198, 90, 0], [202, 183, 228]],
    [[247, 60, 0], [169,  13, 253]],
    [[285, 60, 0], [171, 154, 179]],
    [[247, 90, 0], [208,  81, 133]],
    [[285, 90, 0], [239, 208, 157]],
    [[90,  36, 0], [136, 110,  67]],
    [[150, 36, 0], [ 40,  75, 238]],
    [[210, 36, 0], [ 96, 166,  55]],
    [[270, 36, 0], [104, 238, 232]],
    [[75,  60, 1], [125, 246, 223]],
    [[112, 60, 1], [208, 144, 245]],
    [[75,  90, 1], [207,  23,  14]],
    [[112, 90, 1], [234, 142,  58]],
    [[161, 60, 1], [188,  51,  12]],
    [[198, 60, 1], [ 82,  66,  87]],
    [[161, 90, 1], [ 69,  43, 128]],
    [[198, 90, 1], [135, 196, 115]],
    [[247, 60, 1], [  1,  41, 204]],
    [[285, 60, 1], [209,  35, 145]],
    [[247, 90, 1], [233,  12, 193]],
    [[285, 90, 1], [220,  74, 251]],
    [[90,  36, 1], [ 71, 219,  13]],
    [[150, 36, 1], [174, 224, 159]],
    [[210, 36, 1], [106, 247,  93]],
    [[270, 36, 1], [154,  87, 250]],
    [[75,  60, 2], [  0,   0,   0]],
    [[112, 60, 2], [184,  35,  83]],
    [[75,  90, 2], [117,  57, 147]],
    [[112, 90, 2], [205, 159, 245]],
    [[161, 60, 2], [243, 187, 114]],
    [[198, 60, 2], [197, 139, 227]],
    [[161, 90, 2], [192, 228, 216]],
    [[198, 90, 2], [ 21, 197, 132]],
    [[247, 60, 2], [218, 122, 152]],
    [[285, 60, 2], [178,  80,  70]],
    [[247, 90, 2], [248, 178,  31]],
    [[285, 90, 2], [118, 250,   6]],
    [[90,  36, 2], [218, 171,  23]],
    [[150, 36, 2], [ 91, 212,  71]],
    [[210, 36, 2], [205, 201, 119]],
    [[270, 36, 2], [202, 102,  52]]
]

print(len(LOCATIONS))
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
    Returns the color list ready to be fed into map.replot
    '''
    
    colors = []
    
    for i in range(len(LOCATIONS)):
        colors.append(LOCATIONS[owner(players,i)][1])
        
    return colors
    
def generate_legend(players):
    legend = generate_color_list(VANILLA_PLAYERS)
    
    for i in range(len(players)):
        if players[i] == []:
            legend[i] = [255,255,255]
            
    return legend 


VANILLA_PLAYERS = read_players("vanilla_state.txt")

if mode == 0 or mode==1:
    if mode == 0:
        players = read_players("vanilla_state.txt")
    elif mode == 1:    
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
    
    random_location = secrets.randbelow(len(LOCATIONS))
    near_locations = nearest(players, random_location)
    
    if near_locations is not None:
        target_location = secrets.choice(near_locations)
        
        winner = owner(players, random_location)
        loser = owner(players, target_location)

        players[loser].remove(target_location)
        players[winner].append(target_location)
        
        print(NAMES[winner] + " ha occupato l'ufficio di " + NAMES[loser]+ ".")
        if players[loser] == []:
            print(NAMES[loser] + " è stato completamente sconfitto")
        
        legend = generate_legend(players)
        new_colors = generate_color_list(players)
       
        if mode == 2:
            map.replot(legend, new_colors, 0)
        elif mode == 3:
            map.replot(legend, new_colors, 1)
            write_players(players, "saved_state.txt")
    else:
        print(winner)

elif mode == 4 or mode == 5:    
    winners = [0] * len(LOCATIONS)
    
    for i in range(GAME_NUMBER):
        if mode == 4:
            players = read_players("vanilla_state.txt")
        elif mode == 5:
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
    plt.xticks(range(len(LOCATIONS)), NAMES, rotation=90, fontsize=10)
    plt.title("z= " + str(Z_DIST) + " N=" + str(GAME_NUMBER))
    plt.show()
    
elif mode == 6 or mode == 7:
    game_lenghts = []
    
    for i in range(GAME_NUMBER):
        if mode == 6:
            players = read_players("vanilla_state.txt")
        elif mode == 7:
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
    
elif mode == 9 or mode == 10:
    if mode == 9:
        players = read_players("vanilla_state.txt")
    elif mode == 10:
        players = read_players("saved_state.txt")
        
    colors = generate_color_list(players)
    map.replot(colors, colors, 1)  