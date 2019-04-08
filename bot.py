# -*- coding: utf-8 -*-

from math import sin, cos, sqrt, atan2, radians
import random

# Raggio terrestre
R = 6373.0

LOCATIONS = [
    # Nome                  Longitudine         Latitudine
    ["Cuneo",               7.5738751700989440, 44.478425321838050], 
    ["Bologna",             11.343112711393536, 44.430901941929270], 
    ["Grosseto",            11.244584245610612, 42.788822341391906], 
    ["Torino",              7.4301865601029470, 45.145151007409740], 
    ["Caserta",             14.157425303562738, 41.217465291965840], 
    ["Alessandria",         8.6630740165041100, 44.831180602613910], 
    ["Ancona",              13.153818501495640, 43.504782165103860], 
    ["MedioCampidano",      8.7507662615331440, 39.562885947706526], 
    ["Modena",              10.888317020554469, 44.534015028283164], 
    ["Lodi",                9.5810171534997970, 45.233327161557430], 
    ["Novara",              8.5503793110202440, 45.571494274170730], 
    ["Avellino",            15.079084364782188, 40.977990806138120], 
    ["Verona",              11.038341476957600, 45.419383449630580], 
    ["AscoliPiceno",        13.551648156756684, 42.888832984301650], 
    ["Caltanissetta",       14.069087916490346, 37.358046462242560], 
    ["Rovigo",              11.917578771312067, 45.016085669962635], 
    ["Catania",             14.827521851787353, 37.513610885143500], 
    ["Treviso",             12.222285351753932, 45.797296842504380], 
    ["Ogliastra",           9.5148137998692790, 39.895661957651870], 
    ["Livorno",             10.476963353241525, 43.145480005618110], 
    ["OlbiaTempio",         9.2936854747111110, 40.895725127053920], 
    ["Bergamo",             9.7866046733162600, 45.794712746882740], 
    ["Bolzano",             11.404594181282246, 46.694340033087070], 
    ["Napoli",              14.344014763515625, 40.850230078016800], 
    ["Campobasso",          14.775500592855442, 41.707653499060830], 
    ["Fermo",               13.573190700927430, 43.097468949223200], 
    ["Roma",                12.570620081134650, 41.920490850988000], 
    ["Lucca",               10.436879267966930, 44.003644319543640], 
    ["Brescia",             10.317585187986353, 45.706918903084635], 
    ["Piacenza",            9.6240401527073660, 44.869745631104834], 
    ["Agrigento",           13.505221255217755, 37.432736797593314], 
    ["Pistoia",             10.848439019365486, 43.968295011272850], 
    ["ForliCesena",         12.037385827114026, 44.038477692195760], 
    ["Pescara",             13.984360224866682, 42.331351273884906], 
    ["Vercelli",            8.2091418732754760, 45.527608811967190], 
    ["Genova",              9.1171448957444030, 44.470019068015880], 
    ["Enna",                14.428595597300427, 37.580445450251590], 
    ["Pavia",               9.0328967885320550, 45.110132769784790], 
    ["Nuoro",               9.3012529061434870, 40.303522639715446], 
    ["Trieste",             13.765047699846697, 45.683550502384854], 
    ["Aosta",               7.3708038328103690, 45.730303044135860], 
    ["Firenze",             11.291863397102532, 43.819919978107810], 
    ["Trapani",             12.706427131101913, 37.810272831956660], 
    ["Teramo",              13.724071715005987, 42.646549235786910], 
    ["Udine",               13.157742679272133, 46.225604538456224], 
    ["VerbanoCusioOssola",  8.3360934078600300, 46.085444652999130], 
    ["Frosinone",           13.532663933996613, 41.614766703976850], 
    ["Taranto",             17.201101284417680, 40.541577880790100], 
    ["Catanzaro",           16.489082193899492, 38.896505052297950], 
    ["Belluno",             12.179976668293524, 46.311217235678185], 
    ["Pordenone",           12.692689941837553, 46.107692896012200], 
    ["Viterbo",             11.992884864465012, 42.425143132286630], 
    ["Gorizia",             13.497501397542860, 45.857085135870435], 
    ["Ferrara",             11.846930946114963, 44.789146773047160], 
    ["Chieti",              14.378069932118322, 42.102342657908700], 
    ["Crotone",             16.949654265927386, 39.177350455065266], 
    ["Foggia",              15.557136061432757, 41.541281329614584], 
    ["Perugia",             12.528462906447464, 43.065977560968925], 
    ["ViboValentia",        16.162948219511794, 38.625271435078780], 
    ["Bari",                16.757281037483622, 40.932212546421376], 
    ["Benevento",           14.750865426648190, 41.240138880273720], 
    ["MassaCarrara",        10.002958356898057, 44.257897476559020], 
    ["Pisa",                10.667520102479662, 43.503687932924485], 
    ["Latina",              13.145134099428994, 41.430569366457100], 
    ["Salerno",             15.223941493069480, 40.440548234332155], 
    ["Messina",             14.941159591457897, 38.038342704466540], 
    ["Lecco",               9.3866565780278210, 45.904925761045980], 
    ["Lecce",               18.178597392097700, 40.175340483251540], 
    ["Varese",              8.7799933965733600, 45.790598299081630], 
    ["Como",                9.1498201032510130, 45.932829845001960], 
    ["BarlettaAndriaTrani", 16.166681153515462, 41.173283320617170], 
    ["Ragusa",              14.682256731721564, 36.908474222404436], 
    ["Macerata",            13.239836692584973, 43.190125674143790], 
    ["Imperia",             7.7951410130960000, 43.951115203136360], 
    ["PesaroeUrbino",       12.672618286119860, 43.704756494314815], 
    ["Palermo",             13.587458596505371, 37.870397653249796], 
    ["Matera",              16.447173058044598, 40.468513898854360], 
    ["Vicenza",             11.492392644100166, 45.672527988097066], 
    ["Biella",              8.0894643596411710, 45.582685915150610], 
    ["LAquila",             13.595461593911487, 42.105804452774960], 
    ["Milano",              9.1187127253829380, 45.463591552843510], 
    ["Rieti",               12.952426414553678, 42.373791303421980], 
    ["Potenza",             15.884012189281284, 40.516132998300620], 
    ["Oristrano",           8.7215525238910540, 39.988084042982260], 
    ["Brindisi",            17.692864245883477, 40.610337920858750], 
    ["Cagliari",            9.1653519575425620, 39.378297843336000], 
    ["ReggioCalabria",      16.025704658423140, 38.240432697758465], 
    ["CarboniaIglesias",    8.5623641735416970, 39.210221177048400], 
    ["Asti",                8.1844399502548540, 44.877445543824340], 
    ["Ravenna",             11.994487147860877, 44.371913673168680], 
    ["Siena",               11.454446407553494, 43.193133738517780], 
    ["Savona",              8.2852109874570270, 44.285589164393890], 
    ["Mantova",             10.772684256261762, 45.124612133809190], 
    ["ReggioEmilia",        10.550334001283565, 44.605885104078110], 
    ["Rimini",              12.442960341208350, 43.939094175429690], 
    ["LaSpezia",            9.7263447369445690, 44.226388727598810], 
    ["Prato",               11.091924479629201, 43.951318718557160], 
    ["Siracusa",            15.030631729875170, 37.076998799037284], 
    ["Cosenza",             16.321922330756390, 39.564409805294815], 
    ["Sondrio",             9.9142784390094680, 46.298421499945710], 
    ["Padova",              11.809764253908115, 45.354554096391020], 
    ["Cremona",             10.002179112279500, 45.222349024568600], 
    ["MonzaBrianza",        9.2687472478492020, 45.632322303699176], 
    ["Isernia",             14.242854660835814, 41.645991920475750], 
    ["Trento",              11.129860630914095, 46.138238005676710], 
    ["Terni",               12.371519308743661, 42.660273271106640], 
    ["Parma",               10.046238197502134, 44.670988188409325], 
    ["Venezia",             12.478961975136153, 45.528302856209000], 
    ["Sassari",             8.6984202705593660, 40.628353822192940], 
    ["Arezzo",              11.855923561810323, 43.535613304023215]
]

def geodetic_distance(location1, location2):
    # https://stackoverflow.com/a/19412565

    lon1 = radians(location1[1])
    lat1 = radians(location1[2])
    lon2 = radians(location2[1])
    lat2 = radians(location2[2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
    
def nearest(location):
    '''
    Returns the location nearest to the given one, based on minimum
    'geodetic_distance', excluding locations already occupied by the owner.
    Returns None if the owner occupies all locations.
    
    find_nearest(3) -> 40
    (3: Torino, 40: Aosta)
    '''
    
    current_owner = owner(location)
    excluded_players = players[current_owner]
    
    nearest = None
    min_distance = float("inf")  
    
    for i in range(len(LOCATIONS)):
        if i in excluded_players: continue
        distance = geodetic_distance(LOCATIONS[current_owner], LOCATIONS[i])
        if distance < min_distance:
            min_distance = distance
            nearest = i
            
    return nearest

def owner(location):
    '''
    Returns the owner of the given location
    
    owner(3) -> 3
    '''
    for i in range(len(players)):
        if location in players[i]:
            return i

# Game inizialization
players = []

# Vanilla start
for i in range(len(LOCATIONS)):
    # Every player owns itself
    players.append([i])

# # Given start
# for i in range(len(LOCATIONS)):
#     # Every player owns itself
#     players.append([])
#
# # VBO
# players[45] = [0,3,4,9,10,12,21,22,28,29,34,35,37,40,45]
# # Rovigo
# players[15] = [1,6,8,13,15,25,26,31,32,33,41,43,46,51,53]
# # Lucca
# players[27] = [27]
# # Taranto
# players[47] = [4,11,23,24,47,48]
# # Gorizia
# players[52] = [17,39,44,49,50,52]
# # Ragusa
# players[71] = [14,16,30,36,42]
# # Carbonia-Iglesias
# players[87] = [2,7,18,19,20,38]
# # Isernia
# players[103] = [103]
    

    
while True:
    random_location = random.choice(range(len(LOCATIONS))) #TODO Migliorabile
    target_location = nearest(random_location)

    if target_location is not None:    
        winner = owner(random_location)
        loser = owner(target_location)
    
        players[loser].remove(target_location)
        players[winner].append(target_location)
    else:
        print(LOCATIONS[owner(0)][0])
        break