import random
import pygame


class Snake():
    def __init__(self, snake_color):
        self.snake_head_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def validate(self):
        # изменение направления
        if any(
                (self.change_to == 'RIGHT' and not self.direction == 'LEFT',
                 self.change_to == 'LEFT' and not self.direction == 'RIGHT',
                 self.change_to == 'UP' and not self.direction == 'DOWN',
                 self.change_to == 'DOWN' and not self.direction == 'UP')
        ):
            self.direction = self.change_to

    def head_change_position(self):
        # изменение позици головы
        if self.direction == 'RIGHT':
            self.snake_head_pos[0] += 10
        elif self.direction == 'LEFT':
            self.snake_head_pos[0] -= 10
        elif self.direction == 'UP':
            self.snake_head_pos[1] -= 10
        elif self.direction == 'DOWN':
            self.snake_head_pos[1] += 10

    def body_mechanism(self, score, food_pos, screen_width, screen_height):
        # если вставлять просто snake_head_pos,
        # то на всех трех позициях в snake_body
        # окажется один и тот же список с одинаковыми координатами
        self.snake_body.insert(0, list(self.snake_head_pos))
        # если поглотила еду
        if (self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]):
            # рандомим следующее положение еды
            food_pos = [random.randrange(1, screen_width/10)*10,
                        random.randrange(1, screen_height/10)*10]
            score +=1
        else:
            # если не нашли еду убираем 1 сегмент иначе змея будет всё время расти
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        # сегменты змеи
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_for_strike(self, game_over, screen_width, screen_height):
        # проверка столкновений
        if any(
                (self.snake_head_pos[0] > screen_width-10
                 or self.snake_head_pos[0] < 0,
                 self.snake_head_pos[1] > screen_height-10
                 or self.snake_head_pos[1] < 0)
        ):
            game_over()
        for block in self.snake_body[1:]:
            # проверка столкновений с сегментами
            if (block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]):
                game_over()
