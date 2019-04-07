
# coding: utf-8

# In[472]:



import pygame
import pygame as pg
import numpy as np
import random

#Colors
white = (255,255,255)
black = (0,0,0),

L = 40

#Open the screen
screen = pg.display.set_mode((400,650))
screen.fill(white)

L = 30
id = 0

#officeid[j] = (#id_office, floor, (x,y) barycenter, [color coord])
officeid = []


for floor in range (0,3):
    for k in range(0,3):
        for j in range(1, 5):
            for i in range (0, 2):

                color1 = random.randint(0,255)
                color2 = random.randint(0,255)
                color3 = random.randint(0,255)

                rect_im = pg.draw.rect(screen, pygame.Color(color1, color2, color3), (i*1.25*L + 2*L + k*2.875*L, j*L + L + floor*7*L, L, L), 0)
                rect = pygame.Rect(i*1.25*L + 2*L + k*2.875*L, j*L + L + floor*7*L, L, L)
                center = rect.center
                temp = np.array([id, int(floor) , center, np.array([color1, color2, color3])])
                np.array(officeid.append(temp))
                id = id + 1                
                
                
    for i in range(0,8):
        
        color1 = random.randint(0,255)
        color2 = random.randint(0,255)
        color3 = random.randint(0,255)

        
        pg.draw.rect(screen, pygame.Color(color1, color2, color3), (i*L + 2*L, 0.7*L + 7*floor*L, L, L), 0)
        rect = pygame.Rect(i*L + 2*L, 0.7*L + 7*floor*L, L, L)
        center = rect.center
        temp = np.array([id, int(floor) , center, np.array([color1, color2, color3])])
        np.array(officeid.append(temp))
        id = id + 1     


    pg.draw.lines(screen, black, False, [(2*L, 0.7*L + 7*floor*L), (9.98*L, 0.7*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(2*L, 5.98*L + 7*floor*L), (4.23*L, 5.98*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(7.1*L, 6*L + 7*floor*L), (7.1*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(4.8*L, 6*L + 7*floor*L), (7.1*L, 6*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(4.23*L, 2*L + 7*floor*L), (4.8*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(7.1*L, 2*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(4.23*L, 6*L + 7*floor*L), (4.23*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(4.82*L, 6*L + 7*floor*L), (4.82*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (7.7*L, 2*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(2*L, 0.73*L + 7*floor*L), (2*L, 6*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(9.98*L, 0.73*L + 7*floor*L), (9.98*L, 6*L + 7*floor*L)], 2)
    pg.draw.lines(screen, black, False, [(7.7*L, 6*L + 7*floor*L), (10*L, 6*L + 7*floor*L)], 2)


#image.fill(color, rect)

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


# In[353]:


print(np.array(officeid)[20])

