from board import Board
from player import Player
from food_manager import FoodManager
from setup import *


class Game:
    def __init__(self):
        self.board = Board()
        self.food_manager = FoodManager() 
        self.snake = Player(center - 2 * x_unit)

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            elif event.type == pygame.KEYDOWN:
                self.snake.get_input(event)
        self.food_manager.update(self.snake.body)
        status = self.snake.update(delta, self.food_manager)
        if len(self.snake.body) == LENGTH * HEIGHT:
            return COMMAND_WIN
        if status == COMMAND_LOSE:
            return status
        return
                
               

    def draw(self, screen):
        self.board.draw(screen)
        self.snake.draw(screen)
        self.food_manager.draw(screen)