import pygame as pg
import pygame.time


class Color:
    def __init__(self, r, g, b):
        self.rgb = (r, g, b)


red = Color(193, 11, 11)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)
gray = Color(100, 100, 100)
black = Color(0, 0, 0)
blueT = Color(120, 230, 142)
white = Color(255, 255, 255)

# def move(move_what, xx=0, yy=0):
#


pg.init()
size = (600, 400)
screen = pg.display.set_mode(size)
pg.display.set_caption('Моя программа')
font = pg.font.SysFont('comicsansms', 40)
follow = font.render('Hi, I am very hungry!', 1, black.rgb, red.rgb)
too = font.render('I am 2 and go fack my ass', 1, green.rgb, blue.rgb)
width, height = too.get_size()
x, y = 0, 300
direct_x = 1
direct_y = 1
FPS = 75
clock = pygame.time.Clock()


class Action:
    def move(self, xx, yy, direct_xx=1, direct_yy=1):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
            __width, __height = self.get_size()
            clock.tick(60)
            screen.fill(black.rgb)
            screen.blit(self, (xx, yy))
            if xx >= 600 - __width or xx < 0:
                direct_xx = -direct_xx
            if yy + __height >= 400 or yy < 0:
                direct_yy = -direct_yy
            xx += direct_xx
            yy += direct_yy
            pg.display.update()


Action.move(follow, 0, 0)
Action.move(too, 300, 200)
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             quit()
#
#     screen.fill(black.rgb)
#     clock.tick(FPS)
#     screen.blit(follow, (0, 0))
#     screen.blit(too, (x, y))
#     if x >= 600-width or x < 0:
#         direct_x = -direct_x
#     if y >= 400-height or y < 0:
#         direct_y = -direct_y
#     x += direct_x
#     y += direct_y
#     pg.display.update()
