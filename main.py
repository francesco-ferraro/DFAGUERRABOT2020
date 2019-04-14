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
# 9 - schermata iniziale
# 10 - testing
mode = 2

GAME_NUMBER = 5000

Z_DIST = 90

# c = [[ 41,  49, 104],
# [231, 113,  93],
# [225, 188, 132],
# [217, 115,  13],
# [ 74,  88, 165],
# [194,  54,  23],
# [237, 122, 189],
# [ 43,  79, 209],
# [238, 211,  94],
# [114,  19, 196],
# [ 91, 220, 201],
# [ 55, 169,  30],
# [211,  63,  31],
# [ 23, 126,  13],
# [146, 111,  36],
# [221,  29, 232],
# [ 54, 238, 118],
# [ 78, 229,  62],
# [82, 16, 29],
# [ 14, 244, 226],
# [211,  29,  12],
# [252, 250, 105],
# [169,   5, 169],
# [ 56, 127,  96],
# [ 26, 108,  84],
# [101, 111, 179],
# [  8, 207, 215],
# [248, 203, 243],
# [236, 159,  14],
# [234, 141, 194],
# [173,  69, 149],
# [116, 183, 127],
# [232,  41, 119],
# [ 62, 156,   8],
# [109, 175,  39],
# [231, 178, 254],
# [ 7, 90, 46],
# [  3, 116, 165],
# [ 61, 190, 192],
# [245, 218, 110],
# [ 92, 110, 185],
# [104,  96, 202],
# [157,  56,  78],
# [211, 107, 103],
# [ 66, 152, 102],
# [248,  54,  96],
# [101,  58, 134],
# [28, 31, 78]]

LOCATIONS = [
    [[75,  60, 0], [ 41,  49, 104]],
    [[112, 60, 0], [231, 113,  93]],
    [[75,  90, 0], [225, 188, 132]],
    [[112, 90, 0], [217, 115,  13]],
    [[161, 60, 0], [ 74,  88, 165]],
    [[198, 60, 0], [194,  54,  23]],
    [[161, 90, 0], [237, 122, 189]],
    [[198, 90, 0], [ 43,  79, 209]],
    [[247, 60, 0], [238, 211,  94]],
    [[285, 60, 0], [114,  19, 196]],
    [[247, 90, 0], [ 91, 220, 201]],
    [[285, 90, 0], [ 55, 169,  30]],
    [[90,  36, 0], [211,  63,  31]],
    [[150, 36, 0], [ 23, 126,  13]],
    [[210, 36, 0], [146, 111,  36]],
    [[270, 36, 0], [221,  29, 232]],
    [[75,  60, 1], [ 54, 238, 118]],
    [[112, 60, 1], [ 78, 229,  62]],
    [[75,  90, 1], [82,   16,  29]],
    [[112, 90, 1], [ 14, 244, 226]],
    [[161, 60, 1], [211,  29,  12]],
    [[198, 60, 1], [252, 250, 105]],
    [[161, 90, 1], [169,   5, 169]],
    [[198, 90, 1], [ 56, 127,  96]],
    [[247, 60, 1], [ 26, 108,  84]],
    [[285, 60, 1], [101, 111, 179]],
    [[247, 90, 1], [  8, 207, 215]],
    [[285, 90, 1], [248, 203, 243]],
    [[90,  36, 1], [236, 159,  14]],
    [[150, 36, 1], [234, 141, 194]],
    [[210, 36, 1], [173,  69, 149]],
    [[270, 36, 1], [116, 183, 127]],
    [[75,  60, 2], [232,  41, 119]],
    [[112, 60, 2], [ 62, 156,   8]],
    [[75,  90, 2], [109, 175,  39]],
    [[112, 90, 2], [231, 178, 254]],
    [[161, 60, 2], [  7,  90,  46]],
    [[198, 60, 2], [  3, 116, 165]],
    [[161, 90, 2], [ 61, 190, 192]],
    [[198, 90, 2], [245, 218, 110]],
    [[247, 60, 2], [ 92, 110, 185]],
    [[285, 60, 2], [104,  96, 202]],
    [[247, 90, 2], [157,  56,  78]],
    [[285, 90, 2], [211, 107, 103]],
    [[90,  36, 2], [ 66, 152, 102]],
    [[150, 36, 2], [248,  54,  96]],
    [[210, 36, 2], [101,  58, 134]],
    [[270, 36, 2], [28, 31, 78]]
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
            map.replot(initial_colors, new_colors)
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
    
elif mode == 9:
    a, b, c = map.initialplot()
    print(a)
    
    # foto 1
    # [array([247, 167, 136]), array([ 46, 102,  77]), array([248,  54, 175]), array([120, 127, 135]), array([94,  1, 70]), array([136, 187, 130]), array([210, 147,  93]), array([121, 237,  96]), array([113,  75, 173]), array([ 81,  63, 225]), array([210,  29, 214]), array([119, 185, 183]), array([219, 235,  15]), array([ 14, 100, 175]), array([154,  34,  12]), array([212, 196, 207]), array([ 96, 236,  96]), array([209, 109,   3]), array([ 57, 204,  81]), array([226, 240, 151]), array([163, 223,  80]), array([168,  85,  73]), array([ 13, 234, 203]), array([ 4,  7, 35]), array([223, 249,  72]), array([ 42, 147,  64]), array([ 29, 162, 240]), array([145, 191, 207]), array([144, 103, 177]), array([188,  33, 176]), array([104, 171,  80]), array([238, 104, 133]), array([172, 231, 238]), array([  5, 122, 197]), array([218, 102, 227]), array([195,  67, 188]), array([161, 145, 188]), array([183,  61,  60]), array([209,  90, 254]), array([170, 141, 107]), array([239,  45, 210]), array([203, 162,  13]), array([ 52,  45, 212]), array([223, 206, 242]), array([218, 159, 172]), array([134,  50,   7]), array([75, 70, 71]), array([221, 206, 247])]
    
    # foto 2
    # [array([120, 138, 150]), array([127, 132, 111]), array([ 43, 235,  41]), array([200, 221, 205]), array([195,  83, 143]), array([196, 132, 195]), array([ 31, 106,  81]), array([214, 203,  83]), array([227, 131, 168]), array([101,  53, 237]), array([ 50, 134,  15]), array([128,  83,  20]), array([135,  64, 253]), array([213, 158, 190]), array([  6, 223, 182]), array([ 29, 114,  65]), array([ 24, 239, 248]), array([154, 228,  91]), array([20, 67, 13]), array([ 53, 118, 107]), array([226, 203, 110]), array([115, 149, 166]), array([188, 244,  88]), array([187,  49, 184]), array([166, 248, 138]), array([158,  26,  73]), array([185, 177, 146]), array([223,  40, 103]), array([223,  54,  54]), array([ 51, 203, 236]), array([130, 247, 104]), array([216,  35, 114]), array([ 16,  87, 104]), array([129,   4, 156]), array([214,   5, 128]), array([ 68, 135,  56]), array([183, 189,   3]), array([ 54, 163, 100]), array([ 84, 133, 124]), array([ 57, 195,  96]), array([ 19, 224, 150]), array([103, 115, 210]), array([ 33, 220,  21]), array([ 28,  98, 200]), array([229,   7,  37]), array([165,  35,  65]), array([102,  96, 116]), array([172,  70, 110])]
    
    # foto 3
    # [array([138, 117, 181]), array([152, 179,  43]), array([203,  46,  26]), array([104, 168, 219]), array([105, 245, 230]), array([116, 161, 177]), array([165, 181, 123]), array([189, 210, 111]), array([217, 247, 246]), array([193, 213, 119]), array([236, 177, 239]), array([ 51, 133, 121]), array([ 81, 113,   0]), array([139, 193,  86]), array([197, 132, 129]), array([110, 111, 141]), array([206,  18,  18]), array([ 43,  48, 213]), array([223,   8,  13]), array([248, 223, 151]), array([59, 89, 45]), array([216, 210, 223]), array([162,  58,  55]), array([150, 207, 218]), array([159,  93,  17]), array([199, 164,  86]), array([210,   8, 255]), array([233, 212,  16]), array([135, 220,  86]), array([228,   4,  23]), array([228, 122, 123]), array([196, 135, 214]), array([83, 72, 93]), array([130,  32, 107]), array([247, 225, 219]), array([  9, 166,  14]), array([ 52, 175,  88]), array([ 19, 193, 190]), array([112,  89, 144]), array([ 71, 167,  75]), array([123, 232, 244]), array([242,  21, 162]), array([ 90,  12, 178]), array([ 50, 116, 152]), array([193, 101, 248]), array([190, 134, 203]), array([144, 181, 118]), array([214,  39,  69])]
    
    # 4
    # [array([243,  71, 191]), array([148, 144,  23]), array([ 50, 184, 120]), array([228, 125, 216]), array([251, 235, 167]), array([163, 105,  20]), array([144, 170,  70]), array([ 30, 216,  33]), array([182,  43, 169]), array([ 28,  50, 122]), array([215,   6, 227]), array([254, 116,  16]), array([15,  3, 22]), array([239, 249, 115]), array([ 42,  68, 198]), array([154,  15, 106]), array([ 50, 101, 226]), array([ 26,  80, 173]), array([ 39,  84, 145]), array([205,  20, 157]), array([177,  76, 208]), array([147, 204,  36]), array([ 18,  28, 181]), array([210, 143, 192]), array([ 22, 227,  58]), array([104, 175,  88]), array([241,  38, 131]), array([182,   1, 228]), array([115, 139,  96]), array([  2,  51, 141]), array([ 80, 143, 200]), array([16,  5, 36]), array([ 43, 194, 110]), array([229, 181,  66]), array([ 19, 184,  11]), array([183, 133, 240]), array([227,  23,  71]), array([ 34,  49, 170]), array([141, 160,  70]), array([ 50, 103, 151]), array([248,  36, 237]), array([ 61, 218, 201]), array([106, 212, 247]), array([  7, 153,  31]), array([ 66,  63, 178]), array([196, 205,  95]), array([ 78, 191,  78]), array([ 98, 233, 110])]
    
    # 5
    # [array([144, 109,  60]), array([99, 47, 63]), array([210,  34, 161]), array([154,  79, 170]), array([ 21, 125, 180]), array([ 44, 221, 240]), array([203, 112,  50]), array([184, 167, 174]), array([248, 115, 183]), array([102, 141,   3]), array([ 41, 213,  14]), array([ 42,  49, 220]), array([ 35,  50, 218]), array([101, 184,  17]), array([188,  34, 228]), array([ 76, 170, 161]), array([152, 192,  30]), array([235, 243, 238]), array([125, 175, 174]), array([ 34, 248, 118]), array([127, 189,  20]), array([  2, 133,  91]), array([ 6, 41, 62]), array([174, 225,  55]), array([136, 112,   2]), array([147, 100, 188]), array([213, 121, 224]), array([  0, 111, 182]), array([ 61,  50, 164]), array([201,  80,   4]), array([103,  44, 144]), array([ 61,  49, 213]), array([109, 205,  25]), array([ 14, 165,  35]), array([187,   0,  89]), array([ 52,   4, 157]), array([ 43, 216, 145]), array([42, 33, 91]), array([102, 149,  70]), array([185, 234,  73]), array([225, 160, 197]), array([215, 101,  10]), array([ 17,  25, 154]), array([41, 69, 85]), array([  6,  78, 186]), array([ 32,  60, 204]), array([130,  91,  81]), array([ 48, 217, 232])]
    
    # 6
    # [array([122,  59, 224]), array([209, 211, 168]), array([242, 201,  63]), array([43, 23, 59]), array([ 74,  37, 220]), array([223, 208,  54]), array([ 99,  98, 141]), array([ 28,  95, 159]), array([240, 242, 159]), array([ 44, 213,  52]), array([14, 24, 75]), array([251, 219, 219]), array([ 25, 204, 228]), array([ 52, 189,  14]), array([183,  92,  73]), array([159, 133, 239]), array([ 43, 116, 190]), array([112, 208, 172]), array([196, 217, 214]), array([207,  98, 112]), array([175, 222, 190]), array([23,  3, 82]), array([171, 163,  65]), array([203,  90,  19]), array([ 33,  61, 193]), array([ 90,  16, 203]), array([255, 107, 111]), array([251, 124, 130]), array([208,  64,  87]), array([123, 200, 244]), array([192,  10,  30]), array([175, 143, 212]), array([195, 182,  29]), array([217, 169, 108]), array([ 86, 206,  64]), array([129, 241,  71]), array([250, 242, 193]), array([182,  14, 181]), array([81, 16,  6]), array([203,  72,  70]), array([224, 107,  83]), array([166,  86, 212]), array([126, 205, 105]), array([160, 197,  72]), array([174, 143,   9]), array([226, 146, 202]), array([185, 246, 156]), array([ 52, 181, 128])]
    
    # 7
    # [array([250,  47, 206]), array([ 24, 218,  31]), array([209,   9, 229]), array([ 83, 131,  71]), array([26, 93, 52]), array([194, 150,  92]), array([ 28,  93, 137]), array([61,  1, 80]), array([233, 105,   6]), array([143, 208, 169]), array([143, 202, 145]), array([ 23, 243, 165]), array([159, 180, 117]), array([ 55, 240, 121]), array([175, 166, 128]), array([222,   3, 111]), array([ 90, 183,  71]), array([157, 107, 143]), array([ 31,  77, 128]), array([221,  46, 202]), array([135, 251, 192]), array([246, 213, 165]), array([187, 106, 195]), array([ 17,  30, 107]), array([122, 147,  27]), array([ 50,  81, 141]), array([178, 255, 234]), array([ 82, 190,   3]), array([ 87,  19, 239]), array([245, 160, 169]), array([155, 186, 251]), array([101, 116, 124]), array([10, 56, 51]), array([ 67, 216, 138]), array([168, 113,  94]), array([192,  80,  43]), array([ 79, 131, 223]), array([242, 113, 131]), array([131,  97,  23]), array([ 46,  36, 247]), array([177, 240, 186]), array([176,  35, 161]), array([193, 103, 148]), array([246, 185, 192]), array([212, 224, 169]), array([111, 127, 143]), array([250, 127, 182]), array([ 23, 199, 222])]
    
    # 8
    # [array([217, 163,   3]), array([249, 104, 242]), array([245, 154, 126]), array([220, 170, 181]), array([194, 103, 115]), array([170, 166, 145]), array([145, 233, 198]), array([115, 231, 111]), array([ 12, 255, 216]), array([180, 176,  71]), array([184, 136, 235]), array([ 48, 242,  70]), array([226, 216, 102]), array([ 77, 187, 188]), array([136,  22, 196]), array([ 31,   6, 127]), array([169, 172,  30]), array([54, 95, 61]), array([147,  22,  99]), array([206,  64, 152]), array([163, 106,  35]), array([175,  26,  96]), array([118,  61, 209]), array([ 19, 137, 130]), array([ 93, 161,  98]), array([ 13, 225, 128]), array([190, 131, 130]), array([ 97, 120, 213]), array([ 97, 159, 175]), array([137, 144, 245]), array([11, 42, 38]), array([ 60, 118, 205]), array([ 88,  70, 207]), array([ 70,  73, 110]), array([115, 123, 171]), array([203,   5,  88]), array([179,  75,   8]), array([208,   9, 121]), array([ 78, 209, 105]), array([253, 213, 114]), array([148, 133, 151]), array([199, 106, 142]), array([126, 169,  77]), array([150, 165, 217]), array([254,  49,  53]), array([125,  28, 109]), array([221,  56, 133]), array([178, 222, 129])]
    
    # 9
    # [array([155, 202,  47]), array([175, 237, 255]), array([ 17,  53, 179]), array([105,  58, 142]), array([ 54,  98, 169]), array([226,  45, 255]), array([249, 139, 224]), array([202, 183, 228]), array([169,  13, 253]), array([171, 154, 179]), array([208,  81, 133]), array([239, 208, 157]), array([136, 110,  67]), array([ 40,  75, 238]), array([ 96, 166,  55]), array([104, 238, 232]), array([125, 246, 223]), array([208, 144, 245]), array([207,  23,  14]), array([234, 142,  58]), array([188,  51,  12]), array([82, 66, 87]), array([ 69,  43, 128]), array([135, 196, 115]), array([  1,  41, 204]), array([209,  35, 145]), array([233,  12, 193]), array([220,  74, 251]), array([ 71, 219,  13]), array([174, 224, 159]), array([106, 247,  93]), array([154,  87, 250]), array([ 19, 234, 200]), array([184,  35,  83]), array([117,  57, 147]), array([205, 159, 245]), array([243, 187, 114]), array([197, 139, 227]), array([192, 228, 216]), array([ 21, 197, 132]), array([218, 122, 152]), array([ 2, 31, 11]), array([248, 178,  31]), array([118, 250,   6]), array([218, 171,  23]), array([ 91, 212,  71]), array([205, 201, 119]), array([202, 102,  52])]
    
    # 10
    # [array([ 41,  49, 104]), array([231, 113,  93]), array([225, 188, 132]), array([217, 115,  13]), array([ 74,  88, 165]), array([194,  54,  23]), array([237, 122, 189]), array([ 43,  79, 209]), array([238, 211,  94]), array([114,  19, 196]), array([ 91, 220, 201]), array([ 55, 169,  30]), array([211,  63,  31]), array([ 23, 126,  13]), array([146, 111,  36]), array([221,  29, 232]), array([ 54, 238, 118]), array([ 78, 229,  62]), array([82, 16, 29]), array([ 14, 244, 226]), array([211,  29,  12]), array([252, 250, 105]), array([169,   5, 169]), array([ 56, 127,  96]), array([ 26, 108,  84]), array([101, 111, 179]), array([  8, 207, 215]), array([248, 203, 243]), array([236, 159,  14]), array([234, 141, 194]), array([173,  69, 149]), array([116, 183, 127]), array([232,  41, 119]), array([ 62, 156,   8]), array([109, 175,  39]), array([231, 178, 254]), array([ 7, 90, 46]), array([  3, 116, 165]), array([ 61, 190, 192]), array([245, 218, 110]), array([ 92, 110, 185]), array([104,  96, 202]), array([157,  56,  78]), array([211, 107, 103]), array([ 66, 152, 102]), array([248,  54,  96]), array([101,  58, 134]), array([28, 31, 78])]
    
