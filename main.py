from menu import Menu
from game_over import GameOver
from game import Game
from setup import *


is_running = True
delta = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode(dimensions)
scene = Game()

while is_running:
    status = scene.update(delta)
    if status == COMMAND_EXIT:
        is_running = False
    elif status == COMMAND_START:
        scene = Game()
    elif status == COMMAND_LOSE:
        scene = GameOver(len(scene.snake.body), win=False)
    elif status == COMMAND_WIN:
        scene = GameOver(len(scene.snake.body), win=True)
        

    scene.draw(screen)
    pygame.display.flip()
    delta = clock.tick(0)

pygame.quit()
