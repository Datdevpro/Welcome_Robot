import pygame

window = pygame.display.set_mode((500,500))
red = (200,0,0)
rect = (70, 90, 100, 150) # x,y,width,height
rect2 = (335, 90, 100, 150) # x,y,width,height

active = True

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pygame.draw.ellipse(window, red, rect) # DRAW ELLIPSE
    pygame.draw.ellipse(window, red, rect2) 
    pygame.display.update()


