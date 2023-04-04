import pygame
from itertools import cycle

TILE_SIZE = 40
SCREEN_SIZE = pygame.Rect((0, 0, 25*TILE_SIZE, 10*TILE_SIZE))
#screen = pygame.display.set_mode((400, 300))

class Expression(pygame.sprite.Sprite):   # class create object for eyes
    def __init__(self, data):
        super().__init__()
        self.image = pygame.Surface((len(data[0]), len(data))) # set chiều dài và rộng của surface 
        x = y = 0
        for row in data:
            for col in row:
                if col == "O":
                    self.image.set_at((x, y), pygame.Color('green'))
                x += 1
            y += 1
            x = 0
        self.image = pygame.transform.scale(self.image, (TILE_SIZE*len(data[0]), TILE_SIZE*len(data)))
        self.rect = self.image.get_rect()


#create emoji emotion
REGULAR = Expression([             
"                         ",
"                         ",
"    OOOO         OOOO    ",
"   OOOOOO       OOOOOO   ",
"   OOOOOO   O   OOOOOO   ",
"    OOOO    O    OOOO    ",
"                         ",
"                         ",
])

QUESTION = Expression([
"                         ",
"                         ",
"    OOOO                 ",
"   OOOOOO       OOOO     ",
"   OOOOOO      OOOOOO    ",
"    OOOO        OOOO     ",
"                         ",
"                         ",
])

SAD = Expression([
"                         ",
"                         ",
"    OOOOO       OOOOO    ",
"            O            ",
"            O            ",
"            OO           ",
"                         ",
"                         ",
])

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()
    expressions = cycle([REGULAR, SAD, REGULAR, SAD])
    current = next(expressions)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return
            if e.type == pygame.USEREVENT:
                current = next(expressions)

        screen.fill((30, 30, 30))

        screen.blit(current.image, current.rect)
        timer.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()