import pygame
from .constants import BLACK # this is a relative import. ie. in the same package

class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.red_left = self.white_left = 12 # sets 12 pieces per player to be decremented
    self.red_kings = self.white_kings = 0

# win stands for window
  def draw_cubes(self, win):
    win.fill(BLACK)
