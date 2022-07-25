import functions
import pygame
import sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Game')

floor1 = functions.create_floor()
hero1 = functions.create_hero()

def output():
    myfont = pygame.font.SysFont('Arial', 16)
    loc = functions.entrance_to_floor(floor1, hero1)
    str_num = 0
    for _ in range(len(loc)):
        string = ''
        for i in loc[str_num]:
            string += str(i)
            string += '    '                                                       # !!!!!!!!!
        out_str = myfont.render(string.encode('utf-8'), False, (255, 255, 255))    # !!!!!!!!! how can i align "string"
        string = ''                                                                # !!!!!!!!! like a .ljust() method?
        screen.blit(out_str, (10, 10 + str_num * 40))
        str_num += 1

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    output()
    pygame.display.flip()
