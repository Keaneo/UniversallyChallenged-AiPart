import matplotlib as mpl
import pygame
import time
import sys
import numpy as np


#Pygame Values
WINDOW_SIZE = (1280, 720)
BACKGROUND_COLOUR = rgb(0,0,0)
FPS = 60

#Simulation Constraints
roomX = 10
roomY = 10
GRID_SIZE = (roomX, roomY)
PERSON_COLOUR = rgb(60, 230, 20)
OBSTACLE_COLOUR = rgb(140,140,140)
ENTRY_POINT_COLOUR = rgb(20, 30, 230)
EXIT_POINT_COLOUR = rgb(230, 60, 20)



init()
screen = display.set_mode(WINDOW_SIZE)

g = Grid(screen, dimensions=GRID_SIZE)
