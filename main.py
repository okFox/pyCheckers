import pygame
from checkers.constants import WIDTH, HEIGHT

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# define event loop to run X times per second
def main():
  run = True
  clock = pygame.time.Clock()

  while run:
    clock.tick(FPS)
    
    # check event list at each interval
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
