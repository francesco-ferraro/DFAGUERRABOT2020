# -*- coding: utf-8 -*-

from math import sin, cos, sqrt, atan2, radians
import random

# Raggio terrestre
R = 6373.0

# Longitudine, latitudine
territori = {
  "Cuneo": ["Cuneo", 7.573875170098944, 44.47842532183805], 
  "Bologna": ["Bologna", 11.343112711393536, 44.43090194192927], 
  "Grosseto": ["Grosseto", 11.244584245610612, 42.788822341391906], 
  "Torino": ["Torino", 7.430186560102947, 45.14515100740974], 
  "Caserta": ["Caserta", 14.157425303562738, 41.21746529196584], 
  "Alessandria": ["Alessandria", 8.66307401650411, 44.83118060261391], 
  "Ancona": ["Ancona", 13.15381850149564, 43.50478216510386], 
  "Medio-Campidano": ["Medio-Campidano", 8.750766261533144, 39.562885947706526], 
  "Modena": ["Modena", 10.888317020554469, 44.534015028283164], 
  "Lodi": ["Lodi", 9.581017153499797, 45.23332716155743], 
  "Novara": ["Novara", 8.550379311020244, 45.57149427417073], 
  "Avellino": ["Avellino", 15.079084364782188, 40.97799080613812], 
  "Verona": ["Verona", 11.0383414769576, 45.41938344963058], 
  "Ascoli-Piceno": ["Ascoli-Piceno", 13.551648156756684, 42.88883298430165], 
  "Caltanissetta": ["Caltanissetta", 14.069087916490346, 37.35804646224256], 
  "Rovigo": ["Rovigo", 11.917578771312067, 45.016085669962635], 
  "Catania": ["Catania", 14.827521851787353, 37.5136108851435], 
  "Treviso": ["Treviso", 12.222285351753932, 45.79729684250438], 
  "Ogliastra": ["Ogliastra", 9.514813799869279, 39.89566195765187], 
  "Livorno": ["Livorno", 10.476963353241525, 43.14548000561811], 
  "Olbia-Tempio": ["Olbia-Tempio", 9.293685474711111, 40.89572512705392], 
  "Bergamo": ["Bergamo", 9.78660467331626, 45.79471274688274], 
  "Bolzano": ["Bolzano", 11.404594181282246, 46.69434003308707], 
  "Napoli": ["Napoli", 14.344014763515625, 40.8502300780168], 
  "Campobasso": ["Campobasso", 14.775500592855442, 41.70765349906083], 
  "Fermo": ["Fermo", 13.57319070092743, 43.0974689492232], 
  "Roma": ["Roma", 12.57062008113465, 41.920490850988], 
  "Lucca": ["Lucca", 10.43687926796693, 44.00364431954364], 
  "Brescia": ["Brescia", 10.317585187986353, 45.706918903084635], 
  "Piacenza": ["Piacenza", 9.624040152707366, 44.869745631104834], 
  "Agrigento": ["Agrigento", 13.505221255217755, 37.432736797593314], 
  "Pistoia": ["Pistoia", 10.848439019365486, 43.96829501127285], 
  "Forli-Cesena": ["Forli-Cesena", 12.037385827114026, 44.03847769219576], 
  "Pescara": ["Pescara", 13.984360224866682, 42.331351273884906], 
  "Vercelli": ["Vercelli", 8.209141873275476, 45.52760881196719], 
  "Genova": ["Genova", 9.117144895744403, 44.47001906801588], 
  "Enna": ["Enna", 14.428595597300427, 37.58044545025159], 
  "Pavia": ["Pavia", 9.032896788532055, 45.11013276978479], 
  "Nuoro": ["Nuoro", 9.301252906143487, 40.303522639715446], 
  "Trieste": ["Trieste", 13.765047699846697, 45.683550502384854], 
  "Aosta": ["Aosta", 7.370803832810369, 45.73030304413586], 
  "Firenze": ["Firenze", 11.291863397102532, 43.81991997810781], 
  "Trapani": ["Trapani", 12.706427131101913, 37.81027283195666], 
  "Teramo": ["Teramo", 13.724071715005987, 42.64654923578691], 
  "Udine": ["Udine", 13.157742679272133, 46.225604538456224], 
  "Verbano-Cusio-Ossola": ["Verbano-Cusio-Ossola", 8.33609340786003, 46.08544465299913], 
  "Frosinone": ["Frosinone", 13.532663933996613, 41.61476670397685], 
  "Taranto": ["Taranto", 17.20110128441768, 40.5415778807901], 
  "Catanzaro": ["Catanzaro", 16.489082193899492, 38.89650505229795], 
  "Belluno": ["Belluno", 12.179976668293524, 46.311217235678185], 
  "Pordenone": ["Pordenone", 12.692689941837553, 46.1076928960122], 
  "Viterbo": ["Viterbo", 11.992884864465012, 42.42514313228663], 
  "Gorizia": ["Gorizia", 13.49750139754286, 45.857085135870435], 
  "Ferrara": ["Ferrara", 11.846930946114963, 44.78914677304716], 
  "Chieti": ["Chieti", 14.378069932118322, 42.1023426579087], 
  "Crotone": ["Crotone", 16.949654265927386, 39.177350455065266], 
  "Foggia": ["Foggia", 15.557136061432757, 41.541281329614584], 
  "Perugia": ["Perugia", 12.528462906447464, 43.065977560968925], 
  "Vibo-Valentia": ["Vibo-Valentia", 16.162948219511794, 38.62527143507878], 
  "Bari": ["Bari", 16.757281037483622, 40.932212546421376], 
  "Benevento": ["Benevento", 14.75086542664819, 41.24013888027372], 
  "Massa-Carrara": ["Massa-Carrara", 10.002958356898057, 44.25789747655902], 
  "Pisa": ["Pisa", 10.667520102479662, 43.503687932924485], 
  "Latina": ["Latina", 13.145134099428994, 41.4305693664571], 
  "Salerno": ["Salerno", 15.22394149306948, 40.440548234332155], 
  "Messina": ["Messina", 14.941159591457897, 38.03834270446654], 
  "Lecco": ["Lecco", 9.386656578027821, 45.90492576104598], 
  "Lecce": ["Lecce", 18.1785973920977, 40.17534048325154], 
  "Varese": ["Varese", 8.77999339657336, 45.79059829908163], 
  "Como": ["Como", 9.149820103251013, 45.93282984500196], 
  "Barletta-Andria-Trani": ["Barletta-Andria-Trani", 16.166681153515462, 41.17328332061717], 
  "Ragusa": ["Ragusa", 14.682256731721564, 36.908474222404436], 
  "Macerata": ["Macerata", 13.239836692584973, 43.19012567414379], 
  "Imperia": ["Imperia", 7.795141013096, 43.95111520313636], 
  "Pesaro-e-Urbino": ["Pesaro-e-Urbino", 12.67261828611986, 43.704756494314815], 
  "Palermo": ["Palermo", 13.587458596505371, 37.870397653249796], 
  "Matera": ["Matera", 16.447173058044598, 40.46851389885436], 
  "Vicenza": ["Vicenza", 11.492392644100166, 45.672527988097066], 
  "Biella": ["Biella", 8.089464359641171, 45.58268591515061], 
  "L'Aquila": ["L'Aquila", 13.595461593911487, 42.10580445277496], 
  "Milano": ["Milano", 9.118712725382938, 45.46359155284351], 
  "Rieti": ["Rieti", 12.952426414553678, 42.37379130342198], 
  "Potenza": ["Potenza", 15.884012189281284, 40.51613299830062], 
  "Oristrano": ["Oristrano", 8.721552523891054, 39.98808404298226], 
  "Brindisi": ["Brindisi", 17.692864245883477, 40.61033792085875], 
  "Cagliari": ["Cagliari", 9.165351957542562, 39.378297843336], 
  "Reggio-Calabria": ["Reggio-Calabria", 16.02570465842314, 38.240432697758465], 
  "Carbonia-Iglesias": ["Carbonia-Iglesias", 8.562364173541697, 39.2102211770484], 
  "Asti": ["Asti", 8.184439950254854, 44.87744554382434], 
  "Ravenna": ["Ravenna", 11.994487147860877, 44.37191367316868], 
  "Siena": ["Siena", 11.454446407553494, 43.19313373851778], 
  "Savona": ["Savona", 8.285210987457027, 44.28558916439389], 
  "Mantova": ["Mantova", 10.772684256261762, 45.12461213380919], 
  "Reggio-Emilia": ["Reggio-Emilia", 10.550334001283565, 44.60588510407811], 
  "Rimini": ["Rimini", 12.44296034120835, 43.93909417542969], 
  "La-Spezia": ["La-Spezia", 9.726344736944569, 44.22638872759881], 
  "Prato": ["Prato", 11.091924479629201, 43.95131871855716], 
  "Siracusa": ["Siracusa", 15.03063172987517, 37.076998799037284], 
  "Cosenza": ["Cosenza", 16.32192233075639, 39.564409805294815], 
  "Sondrio": ["Sondrio", 9.914278439009468, 46.29842149994571], 
  "Padova": ["Padova", 11.809764253908115, 45.35455409639102], 
  "Cremona": ["Cremona", 10.0021791122795, 45.2223490245686], 
  "Monza-Brianza": ["Monza-Brianza", 9.268747247849202, 45.632322303699176], 
  "Isernia": ["Isernia", 14.242854660835814, 41.64599192047575], 
  "Trento": ["Trento", 11.129860630914095, 46.13823800567671], 
  "Terni": ["Terni", 12.371519308743661, 42.66027327110664], 
  "Parma": ["Parma", 10.046238197502134, 44.670988188409325], 
  "Venezia": ["Venezia", 12.478961975136153, 45.528302856209], 
  "Sassari": ["Sassari", 8.698420270559366, 40.62835382219294], 
  "Arezzo": ["Arezzo", 11.855923561810323, 43.535613304023215]
}

def distanza_geodetica(territorio1, territorio2):
    # https://stackoverflow.com/a/19412565

    lat1 = radians(territori[territorio1][2])
    lon1 = radians(territori[territorio1][1])
    lat2 = radians(territori[territorio2][2])
    lon2 = radians(territori[territorio2][1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
    
def trova_vicino(territorio):
    '''
    Trova il territorio piu vicino a quello dato che non sia già controllato
    dalla provincia che lo controlla

        trova_vicino("Torino") -> "Aosta"
    '''
    territori_esclusi = territori_controllati(provincia_occupante(territorio))
    
    vicino = ""
    distanza_min = float("inf")  
    
    for territorio_i in territori:
        if territorio_i in territori_esclusi: continue
        distanza = distanza_geodetica(territorio, territorio_i)
        if distanza < distanza_min:
            distanza_min = distanza
            vicino = territorio_i
            
    return vicino

def territori_controllati(provincia):
    '''
    Restituisce la lista, anche vuota, dei territori controllati dalla provincia

        territori_controllati('Torino') -> ['Aosta', 'Torino']
        territori_controllati('Aosta')   -> []
    '''
    
    territori_controllati = []
    
    for territorio in territori:
        if territori[territorio][0] == provincia:
            territori_controllati.append(territorio)
    
    return territori_controllati

def provincia_occupante(territorio):
    '''
    Restituisce la provincia che occupa un territorio
    
        provincia_occupante('Aosta') -> 'Torino'
    '''
    
    return territori[territorio][0]
    
def aggiorna_occupante(territorio, provincia):
    territori[territorio][0] = provincia

while True:
    territorio = random.choice(list(territori.keys()))
    provincia = provincia_occupante(territorio)
    nuovo_territorio = trova_vicino(territorio)
    
    try:
        aggiorna_occupante(nuovo_territorio, provincia)
        # print(provincia + " occupa " + nuovo_territorio)
    except:
        print(provincia + " vince")
        break
        
