import map as map

'''
inizializza la mappa: genera i colori degli uffici a random
ritorna i colori degli uffici [[RGB1_uff1, RGB2_uff1, RGB3_uff1]...[RGB1_uff48, RGB2_uff48, RGB3_uff48]]
'''
(color, vettoreperfra, listadist) = map.initialplot()

'''
updatecolor(ufficio sconfitto, ufficio vincitore, color)
ritorna il vettore dei colori aggiornato dopo la battaglia e il vettore che ti serve
'''
#NB: il primo input di map.replot deve essere sempre il vettore color output di map.initialplot()
colorupdated = map.updatecolor(1, 0, color)
(colornew, vettoreperfradopolaguerra) = map.replot(color, colorupdated)
