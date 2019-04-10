# -*- coding: utf-8 -*-

from secrets import randbelow

Z_DIST = 1

LOCATIONS = [
        [0, [75,  60, 0], [69, 177, 110]],
        [1, [112, 60, 0], [153, 30, 207]],
        [2, [75,  90, 0], [29, 226, 154]],
        [3, [112, 90, 0], [15,  20, 188]],
        [4, [117, 120, 1], [15,  20, 188]],
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

while True:
    random_location = randbelow(len(LOCATIONS))
    target_location = nearest(random_location)

    if target_location is not None:    
        winner = owner(random_location)
        loser = owner(target_location)

        players[loser].remove(target_location)
        players[winner].append(target_location)
    else:
        print(winner)
        break