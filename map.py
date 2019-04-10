# coding: utf-8

def initialplot():

    import pygame as pg
    import numpy as np
    import pandas as pd
    import random

    #Colors
    white = (255,255,255)
    black = (0,0,0)
    acquamarine = (78,238,148)
    orchid = (191,62,255)

    L = 30

    # Open the screen
    screen = pg.display.set_mode((800,650))
    screen.fill(white)

    #Title
    pg.init()
    pg.display.set_caption('DFA GUERRA BOT 2020')
    font = pg.font.SysFont('comicsansms', 32)
    text = font.render('DFA war bot 2020', True, orchid, acquamarine)
    textRect = text.get_rect()
    textRect.center = (550, 50)
    screen.blit(text, textRect)
    font = pg.font.SysFont('comicsansms', 14)
    text1 = font.render('Carnera', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 100)
    screen.blit(text1, textRect)
    text1 = font.render('Enrico', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 120)
    screen.blit(text1, textRect)
    text1 = font.render('Lacaprara', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 140)
    screen.blit(text1, textRect)
    text1 = font.render('Vittadini', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 160)
    screen.blit(text1, textRect)
    text1 = font.render('Vittone', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 180)
    screen.blit(text1, textRect)
    text1 = font.render('Sada', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 200)
    screen.blit(text1, textRect)
    text1 = font.render('Mazzocco', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 220)
    screen.blit(text1, textRect)
    text1 = font.render('Monti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 240)
    screen.blit(text1, textRect)
    text1 = font.render('Mengoni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 260)
    screen.blit(text1, textRect)
    text1 = font.render('Baldassarri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 280)
    screen.blit(text1, textRect)
    text1 = font.render('Garuti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 300)
    screen.blit(text1, textRect)
    text1 = font.render('Marastoni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 320)
    screen.blit(text1, textRect)
    text1 = font.render('Zwirner', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 340)
    screen.blit(text1, textRect)
    text1 = font.render('Zanetti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 360)
    screen.blit(text1, textRect)
    text1 = font.render('Fassò', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 380)
    screen.blit(text1, textRect)
    text1 = font.render('Marchetti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 400)
    screen.blit(text1, textRect)
    text1 = font.render('Cololao', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 420)
    screen.blit(text1, textRect)
    text1 = font.render('Garfa', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 440)
    screen.blit(text1, textRect)
    text1 = font.render('Lunardon', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 460)
    screen.blit(text1, textRect)
    text1 = font.render('Feruglio', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 480)
    screen.blit(text1, textRect)
    text1 = font.render('Stella', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 500)
    screen.blit(text1, textRect)
    text1 = font.render('Martucci', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 520)
    screen.blit(text1, textRect)
    text1 = font.render('Zendri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 540)
    screen.blit(text1, textRect)
    text1 = font.render('Lucchesi', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 560)
    screen.blit(text1, textRect)
    text1 = font.render('Benettin', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 580)
    screen.blit(text1, textRect)
    text1 = font.render('Fortunato', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 600)
    screen.blit(text1, textRect)
    text1 = font.render('Giusto', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 100)
    screen.blit(text1, textRect)
    text1 = font.render('Marzari', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 120)
    screen.blit(text1, textRect)
    text1 = font.render('Pierno', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 140)
    screen.blit(text1, textRect)
    text1 = font.render('Mistura', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 160)
    screen.blit(text1, textRect)
    text1 = font.render('Salasnich', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 180)
    screen.blit(text1, textRect)
    text1 = font.render('Stanco', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 200)
    screen.blit(text1, textRect)
    text1 = font.render('Serianni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 220)
    screen.blit(text1, textRect)
    text1 = font.render('Trovato', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 240)
    screen.blit(text1, textRect)
    text1 = font.render('Bottaccin', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 260)
    screen.blit(text1, textRect)
    text1 = font.render('Michieli', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 280)
    screen.blit(text1, textRect)
    text1 = font.render('Borghesani', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 300)
    screen.blit(text1, textRect)
    text1 = font.render('Bastieri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 320)
    screen.blit(text1, textRect)
    text1 = font.render('Patelli', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 340)
    screen.blit(text1, textRect)

    id = 0

    #officeid[j] = (#id_office, floor, (x,y) barycenter, [color coord])
    officeid = []

    #to avoid repeating colors
    rcol = []
    colorv = []

    for floor in range (0,3):
        for k in range(0,3):
            for j in range(1, 3):
                for i in range (0, 2):
                    color1 = random.randint(0,255)
                    color2 = random.randint(0,255)
                    color3 = random.randint(0,255)
                    rcol.append(color1)
                    while color1 in rcol:
                        color1 = random.randint(0,255)

                    rect_im = pg.draw.rect(screen, pg.Color(color1, color2, color3), (i*1.25*L + 2*L + k*2.875*L, 2*j*L + floor*7*L, L, 2*L), 0)
                    rect = pg.Rect(i*1.25*L + 2*L + k*2.875*L, j*L, L, 2*L)
                    center = np.asarray(rect.center).tolist()
                    pos = [center[0], center[1], int(floor)]
                    temp = np.array([id , pos , np.array([color1, color2, color3]).tolist()]).tolist()
                    np.array(officeid.append(temp))
                    colorid = np.array([color1, color2, color3])
                    colorv.append(colorid)
                    id = id + 1


        for i in range(0,4):

            color1 = random.randint(0,255)
            color2 = random.randint(0,255)
            color3 = random.randint(0,255)


            pg.draw.rect(screen, pg.Color(color1, color2, color3), (2*i*L + 2*L, 0.7*L + 7*floor*L, 2*L, L), 0)
            rect = pg.Rect(2*i*L + 2*L, 0.7*L, 2*L, L)
            center = np.asarray(rect.center).tolist()
            pos = [center[0], center[1], int(floor)]
            temp = np.array([id , pos , np.array([color1, color2, color3]).tolist()]).tolist()
            np.array(officeid.append(temp))
            colorid = np.array([color1, color2, color3])
            colorv.append(colorid)
            id = id + 1

        pg.draw.lines(screen, black, False, [(2*L, 0.7*L + 7*floor*L), (9.98*L, 0.7*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(2*L, 5.98*L + 7*floor*L), (4.23*L, 5.98*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.1*L, 6*L + 7*floor*L), (7.1*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.8*L, 6*L + 7*floor*L), (7.15*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.23*L, 2*L + 7*floor*L), (4.8*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.1*L, 2*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.23*L, 6*L + 7*floor*L), (4.23*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.82*L, 6*L + 7*floor*L), (4.82*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(2*L, 0.73*L + 7*floor*L), (2*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(9.98*L, 0.73*L + 7*floor*L), (9.98*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (10*L, 6*L + 7*floor*L)], 2)

    for id in range(0,26):
        legend = pg.draw.rect(screen, pg.Color(int(colorv[id][0]), int(colorv[id][1]), int(colorv[id][2])), (440, 97 + id*20, 10, 10), 0)
    for id in range(27,48):
        legend = pg.draw.rect(screen, pg.Color(int(colorv[id][0]), int(colorv[id][1]), int(colorv[id][2])), (640, 97 + (id-27)*20, 10, 10), 0)

    #To get the id of an office
    #print(officeid)

    pg.display.flip()
    running = True
    while running:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          running = False
          return(colorv, officeid);

def updatecolor(idsconfitto, idvincitore, colorv):
        colorv[idsconfitto][0] = int(colorv[idvincitore][0])
        colorv[idsconfitto][1] = int(colorv[idvincitore][1])
        colorv[idsconfitto][2] = int(colorv[idvincitore][2])
        return(colorv);

def replot(colorv):

    import pygame as pg
    import numpy as np
    import pandas as pd
    import random

    #Colors
    white = (255,255,255)
    black = (0,0,0)
    acquamarine = (78,238,148)
    orchid = (191,62,255)

    L = 30

    # Open the screen
    screen = pg.display.set_mode((800,650))
    screen.fill(white)

    #Title
    pg.init()
    pg.display.set_caption('DFA GUERRA BOT 2020')
    font = pg.font.SysFont('comicsansms', 32)
    text = font.render('DFA war bot 2020', True, orchid, acquamarine)
    textRect = text.get_rect()
    textRect.center = (550, 50)
    screen.blit(text, textRect)
    font = pg.font.SysFont('comicsansms', 14)
    text1 = font.render('Carnera', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 100)
    screen.blit(text1, textRect)
    text1 = font.render('Enrico', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 120)
    screen.blit(text1, textRect)
    text1 = font.render('Lacaprara', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 140)
    screen.blit(text1, textRect)
    text1 = font.render('Vittadini', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 160)
    screen.blit(text1, textRect)
    text1 = font.render('Vittone', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 180)
    screen.blit(text1, textRect)
    text1 = font.render('Sada', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 200)
    screen.blit(text1, textRect)
    text1 = font.render('Mazzocco', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 220)
    screen.blit(text1, textRect)
    text1 = font.render('Monti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 240)
    screen.blit(text1, textRect)
    text1 = font.render('Mengoni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 260)
    screen.blit(text1, textRect)
    text1 = font.render('Baldassarri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 280)
    screen.blit(text1, textRect)
    text1 = font.render('Garuti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 300)
    screen.blit(text1, textRect)
    text1 = font.render('Marastoni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 320)
    screen.blit(text1, textRect)
    text1 = font.render('Zwirner', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 340)
    screen.blit(text1, textRect)
    text1 = font.render('Zanetti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 360)
    screen.blit(text1, textRect)
    text1 = font.render('Fassò', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 380)
    screen.blit(text1, textRect)
    text1 = font.render('Marchetti', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 400)
    screen.blit(text1, textRect)
    text1 = font.render('Cololao', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 420)
    screen.blit(text1, textRect)
    text1 = font.render('Garfa', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 440)
    screen.blit(text1, textRect)
    text1 = font.render('Lunardon', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 460)
    screen.blit(text1, textRect)
    text1 = font.render('Feruglio', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 480)
    screen.blit(text1, textRect)
    text1 = font.render('Stella', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 500)
    screen.blit(text1, textRect)
    text1 = font.render('Martucci', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 520)
    screen.blit(text1, textRect)
    text1 = font.render('Zendri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 540)
    screen.blit(text1, textRect)
    text1 = font.render('Lucchesi', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 560)
    screen.blit(text1, textRect)
    text1 = font.render('Benettin', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 580)
    screen.blit(text1, textRect)
    text1 = font.render('Fortunato', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (400, 600)
    screen.blit(text1, textRect)
    text1 = font.render('Giusto', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 100)
    screen.blit(text1, textRect)
    text1 = font.render('Marzari', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 120)
    screen.blit(text1, textRect)
    text1 = font.render('Pierno', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 140)
    screen.blit(text1, textRect)
    text1 = font.render('Mistura', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 160)
    screen.blit(text1, textRect)
    text1 = font.render('Salasnich', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 180)
    screen.blit(text1, textRect)
    text1 = font.render('Stanco', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 200)
    screen.blit(text1, textRect)
    text1 = font.render('Serianni', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 220)
    screen.blit(text1, textRect)
    text1 = font.render('Trovato', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 240)
    screen.blit(text1, textRect)
    text1 = font.render('Bottaccin', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 260)
    screen.blit(text1, textRect)
    text1 = font.render('Michieli', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 280)
    screen.blit(text1, textRect)
    text1 = font.render('Borghesani', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 300)
    screen.blit(text1, textRect)
    text1 = font.render('Bastieri', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 320)
    screen.blit(text1, textRect)
    text1 = font.render('Patelli', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 340)
    screen.blit(text1, textRect)

    id = 0

    #officeid[j] = (#id_office, floor, (x,y) barycenter, [color coord])
    officeid = []


    for floor in range (0,3):
        for k in range(0,3):
            for j in range(1,3):
                for i in range (0, 2):

                    color1 = int(colorv[id][0])
                    color2 = int(colorv[id][1])
                    color3 = int(colorv[id][2])

                    rect_im = pg.draw.rect(screen, pg.Color(color1, color2, color3), (i*1.25*L + 2*L + k*2.875*L, 2*j*L + floor*7*L, L, 2*L), 0)
                    rect = pg.Rect(i*1.25*L + 2*L + k*2.875*L, j*L, L, 2*L)
                    center = np.asarray(rect.center).tolist()
                    pos = [center[0], center[1], int(floor)]
                    temp = np.array([id , pos , np.array([color1, color2, color3]).tolist()]).tolist()
                    np.array(officeid.append(temp))
                    colorid = np.array([color1, color2, color3])
                    colorv.append(colorid)
                    id = id + 1


        for i in range(0,4):

            color1 = int(colorv[id][0])
            color2 = int(colorv[id][1])
            color3 = int(colorv[id][2])


            pg.draw.rect(screen, pg.Color(color1, color2, color3), (2*i*L + 2*L, 0.7*L + 7*floor*L, 2*L, L), 0)
            rect = pg.Rect(2*i*L + 2*L, 0.7*L, 2*L, L)
            center = np.asarray(rect.center).tolist()
            pos = [center[0], center[1], int(floor)]
            temp = np.array([id , pos , np.array([color1, color2, color3]).tolist()]).tolist()
            np.array(officeid.append(temp))
            colorid = np.array([color1, color2, color3])
            colorv.append(colorid)
            id = id + 1

        pg.draw.lines(screen, black, False, [(2*L, 0.7*L + 7*floor*L), (9.98*L, 0.7*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(2*L, 5.98*L + 7*floor*L), (4.23*L, 5.98*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.1*L, 6*L + 7*floor*L), (7.1*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.8*L, 6*L + 7*floor*L), (7.15*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.23*L, 2*L + 7*floor*L), (4.8*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.1*L, 2*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.23*L, 6*L + 7*floor*L), (4.23*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(4.82*L, 6*L + 7*floor*L), (4.82*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(2*L, 0.73*L + 7*floor*L), (2*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(9.98*L, 0.73*L + 7*floor*L), (9.98*L, 6*L + 7*floor*L)], 2)
        pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (10*L, 6*L + 7*floor*L)], 2)

    for id in range(0,26):
        legend = pg.draw.rect(screen, pg.Color(int(colorv[id][0]), int(colorv[id][1]), int(colorv[id][2])), (440, 97 + id*20, 10, 10), 0)
    for id in range(27,48):
        legend = pg.draw.rect(screen, pg.Color(int(colorv[id][0]), int(colorv[id][1]), int(colorv[id][2])), (640, 97 + (id-27)*20, 10, 10), 0)

    text1 = font.render('Patelli', True, black, white)
    textRect = text1.get_rect()
    textRect.center = (600, 340)
    screen.blit(text1, textRect)

    pg.display.flip()
    running = True
    while running:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          running = False
          return(colorv, officeid);
