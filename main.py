from snake import Snake
from game import Game
from food import Food


if __name__ == '__main__':
    game = Game()
    snake = Snake(game.green)
    food = Food(game.brown, game.screen_width, game.screen_height)

    game.init_errors()
    game.surface_and_title()

    while True:
        snake.change_to = game.event(snake.change_to)
        snake.validate()
        snake.head_change_position()
        game.score, food.food_pos = snake.body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
        snake.draw_snake(game.surface, game.white)
        food.draw_food(game.surface)
        snake.check_for_strike(game.game_over, game.screen_width, game.screen_height)
        game.show_score()
        game.refresh()