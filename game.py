from board import Board
from player import Player
from setup import *


class Game:
    def __init__(self):
        self.board = Board()
        # self.food = 
        self.snake = Player(center)

    def update(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_EXIT
            elif event.type == pygame.KEYDOWN:
                self.snake.get_input(event)
                
               

    def draw(self, screen):
        self.board.draw(screen)
        self.snake.draw(screen)
