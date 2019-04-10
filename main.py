import map

'''
inizializza la mappa: genera i colori degli uffici a random
ritorna i colori degli uffici [[RGB1_uff1, RGB2_uff1, RGB3_uff1]...[RGB1_uff48, RGB2_uff48, RGB3_uff48]]
'''
color = map.initialplot()
'''
updatecolor(ufficio sconfitto, ufficio vincitore, color)
ritorna il vettore dei colori aggironato dopo la battaglia
'''
colorup = map.updatecolor(2, 1, color)
map.replot(colorup)
