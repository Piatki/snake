import pygame
import sys
import time


class Game():
    def __init__(self):
        # размеры окна
        self.screen_width = 720
        self.screen_height = 480
        # определение цветов
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        # частота обновление кадров в секунду
        self.fps_controller = pygame.time.Clock()
        # счётчик
        self.score = 0

    def init_errors(self):
        # проверка запуска определяем переменную
        errors = pygame.init()
        if errors[1] > 0:
            sys.exit()
        else:
            print('OK')

    def surface_and_title(self):
        # задаём рисовательную поверхность и заголовок
        self.surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')

    def event(self, change_to):
        # отслеживание нажатий клавиш игроком
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh(self):
        # обновление экрана
        pygame.display.flip()
        self.fps_controller.tick(23)

    def show_score(self, choice=1):
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black
        )
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.surface.blit(s_surf, s_rect)

    def game_over(self):
        go_font = pygame.font.SysFont('monaco', 24)
        go_surf = go_font.render('Game Over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


