import pygame
import time

pygame.init()

WIDTH =  600
HEIGHT = 600 
scale = (WIDTH,HEIGHT)

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Happy birthday") 

bday = pygame.image.load('bday.jpg')
bday2 = pygame.image.load("bday2.jpg")
bday3 = pygame.image.load("bday3.jpg")

i1 = pygame.transform.scale(bday,scale)
i2 = pygame.transform.scale(bday2,scale)
i3 = pygame.transform.scale(bday3,scale)

font =pygame.font.SysFont("Times New Roman",72)

t1 = font.render("Happy",True, (0,0,0))
t2 = font.render("Birthday!",True,(255,192,203))

t3= font.render("You're so old now!",True, (201,147,212))
text3 = pygame.transform.rotate(t3,45)

t4 = font.render("TMNT",True, (0,128,0))

while True:
    display_surface.blit(i1,(0,0)) 
    display_surface.blit(t1,(200,200))
    display_surface.blit(t2,(180,300))
    pygame.display.update()
    time.sleep(3)
    display_surface.blit(i2,(0,0))
    display_surface.blit(text3,(0,0))
    pygame.display.update()
    time.sleep(3)
    display_surface.blit(i3,(0,0))
    display_surface.blit(t4,(200,30))
    pygame.display.update()
    time.sleep(3)
    
