from menu import Menu
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

    scene.draw(screen)
    pygame.display.flip()
    delta = clock.tick(0)

pygame.quit()
