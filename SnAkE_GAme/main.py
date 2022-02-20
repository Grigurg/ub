import random
import sys

import pygame as pg
import pygame_menu

pg.init()


class SnakeBlock:
    def __init__(self, c_x, c_y):
        self.x = c_x
        self.y = c_y

    def is_inside(self):
        return -1 < self.x < count_blocks and -1 < self.y < count_blocks

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


speed_value = {
    10: 4,
    15: 5,
    25: 6,
    40: 7
}
size_block = 20

blue = (204, 255, 255)
frame_color = (0, 255, 204)
white = (255, 255, 255)
snake_color = (0, 102, 0)

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
snake_eat_color = (224, 0, 0)
count_blocks = 20
margin = 1
header_margin = 70
header_color = (0, 204, 153)
size = [size_block * count_blocks + margin * count_blocks + size_block * 2,
        size_block * count_blocks + margin * size_block + size_block * 2 + header_margin]
print(size)
screen = pg.display.set_mode(size)
pg.display.set_caption('Змейка')
timer = pg.time.Clock()


def draw_block(def_color, def_row, def_column):
    pg.draw.rect(screen, def_color,
                 (size_block + def_column * size_block + margin * (def_column + 1),
                  size_block + header_margin + def_row * size_block + margin * (def_row + 1),
                  size_block, size_block))


def start_game():
    x_snake_eat, y_snake_eat, x_snake_eat2, y_snake_eat2, x_snake_eat1, y_snake_eat1 \
        = None, None, None, None, None, None
    d_row = b_row = 0
    d_col = b_col = 1
    total = 9
    speed = 3

    def head_total():
        font = pg.font.SysFont('Light 300', 50)
        text_total = font.render(f'Total  {total}', True, white)
        text_speed = font.render(f'Speed:  {speed}', True, white)

        screen.blit(text_total, (25, 17))
        screen.blit(text_speed, (250, 17))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT and d_col != -1:
                    b_row = 0
                    b_col = 1
                elif event.key == pg.K_LEFT and d_col != 1:
                    b_row = 0
                    b_col = -1
                elif event.key == pg.K_UP and d_row != 1:
                    b_row = -1
                    b_col = 0
                elif event.key == pg.K_DOWN and d_row != -1:
                    b_row = 1
                    b_col = 0
        screen.fill(frame_color)
        pg.draw.rect(screen, header_color, (0, 0, size[0], header_margin))
        for i in speed_value:
            if total > i:
                speed = speed_value[i]
        if x_snake_eat is None:
            x_snake_eat = random.randint(0, count_blocks - 1)
            y_snake_eat = random.randint(0, count_blocks - 1)
            empty_block = SnakeBlock(x_snake_eat, y_snake_eat)
            while empty_block in snake_blocks:
                x_snake_eat = random.randint(0, count_blocks - 1)
                y_snake_eat = random.randint(0, count_blocks - 1)
                empty_block = SnakeBlock(x_snake_eat, y_snake_eat)
            x_snake_eat, y_snake_eat = empty_block.x, empty_block.y
        if x_snake_eat1 is None:
            x_snake_eat1 = random.randint(0, count_blocks - 1)
            y_snake_eat1 = random.randint(0, count_blocks - 1)
            empty_block1 = SnakeBlock(x_snake_eat, y_snake_eat)
            while empty_block1 in snake_blocks:
                x_snake_eat1 = random.randint(0, count_blocks - 1)
                y_snake_eat1 = random.randint(0, count_blocks - 1)
                empty_block1 = SnakeBlock(x_snake_eat1, y_snake_eat1)
            x_snake_eat1, y_snake_eat1 = empty_block1.x, empty_block1.y
        elif x_snake_eat2 is None:
            x_snake_eat2 = random.randint(0, count_blocks - 1)
            y_snake_eat2 = random.randint(0, count_blocks - 1)
            empty_block2 = SnakeBlock(x_snake_eat2, y_snake_eat2)
            while empty_block2 in snake_blocks:
                x_snake_eat2 = random.randint(0, count_blocks - 1)
                y_snake_eat2 = random.randint(0, count_blocks - 1)
                empty_block2 = SnakeBlock(x_snake_eat, y_snake_eat)
            x_snake_eat2, y_snake_eat2 = empty_block2.x, empty_block2.y
        for row in range(count_blocks):
            for column in range(count_blocks):
                if (column + row) % 2 == 0:
                    color = blue
                else:
                    color = white
                if x_snake_eat == row and y_snake_eat == column or x_snake_eat1 == row and y_snake_eat1 == column\
                        or x_snake_eat2 == row and y_snake_eat2 == column:
                    color = snake_eat_color
                draw_block(color, row, column)
        # draw_block(snake_color, random.randint(0, count_blocks), random.randint(0, count_blocks))
        head = snake_blocks[-1]
        if not head.is_inside():
            break
        d_row = b_row
        d_col = b_col
        head_total()
        for block in snake_blocks:
            draw_block(snake_color, block.x, block.y)
        pg.display.update()
        if x_snake_eat == head.x and y_snake_eat == head.y:
            total += 1
            x_snake_eat, y_snake_eat = None, None
            new_snake_block = SnakeBlock(snake_blocks[0].x - d_row, snake_blocks[1].y - d_col)
            snake_blocks.insert(0, new_snake_block)
        if x_snake_eat1 == head.x and y_snake_eat1 == head.y:
            total += 1
            x_snake_eat1, y_snake_eat1 = None, None
            new_snake_block = SnakeBlock(snake_blocks[0].x - d_row, snake_blocks[1].y - d_col)
            snake_blocks.insert(0, new_snake_block)
        if y_snake_eat2 == head.x and y_snake_eat2 == head.y:
            total += 1
            x_snake_eat2, y_snake_eat2 = None, None
            new_snake_block = SnakeBlock(snake_blocks[0].x - d_row, snake_blocks[1].y - d_col)
            snake_blocks.insert(0, new_snake_block)
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        if new_head in snake_blocks:
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        timer.tick(speed)


menu = pygame_menu.Menu('Welcome', 400, 500,
                        theme=pygame_menu.themes.THEME_SOLARIZED)
menu.add.text_input('Name :', default='')
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
