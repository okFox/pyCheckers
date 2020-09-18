import pygame
from checkersgame.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkersgame.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# define event loop to run X times per second
def main():
  run = True
  clock = pygame.time.Clock()
  board = Board()

  while run:
    clock.tick(FPS)
    
    # check event list at each interval
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  # should quit be capitalized??
        run = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        pass
    board.draw_squares(WIN)
    pygame.display.update()

  pygame.quit()

main()
