import matplotlib as mpl
import pygame
import time
import sys
import numpy as np
from pygame.locals import QUIT, KEYDOWN
from pygame import init, display, event
from pygame import K_ESCAPE, K_BACKSPACE, K_a, K_s, K_g, K_e
from Grid import *


#Pygame Values
WINDOW_SIZE = (1280, 720)
BACKGROUND_COLOUR = (0,0,0)
FPS = 60

#Simulation Constraints
roomX = 10
roomY = 10
GRID_SIZE = (roomX * 10, roomY * 10)
PERSON_COLOUR = (60, 230, 20)
OBSTACLE_COLOUR = (140,140,140)
ENTRY_POINT_COLOUR = (20, 30, 230)
EXIT_POINT_COLOUR = (230, 60, 20)
NUMBER_OF_PEOPLE = 10


init()
screen = display.set_mode(WINDOW_SIZE)
g = Grid(screen, dimensions=GRID_SIZE)

def HillClimb(start=(0, 0), end=(g.x_elems - 1, g.y_elems - 1)):
    g.reset(False)
    """Not the best for open grids"""
    end = g.grid[end[1]][end[0]]
    # Paths to extend
    agenda = [[g.grid[start[1]][start[0]]]]
    # already visited / checked / extended
    extendedList = []

    while agenda:
        path = agenda.pop(0)
        if path[-1] == end:
            for node in path:  # For Drawing the final path
                node.isPath = True
            g.draw()
            display.update()
            print(len(path))
            return  # Return the path (might need it in the future)
        elif path[-1] not in extendedList:  # Check if we visited the current node before or not
            extendedList.append(path[-1])
            a = []  # The paths that will be added to the agenda after being sorted
            for node in path[-1].neighbours:
                # Check if the next node is a wall
                if node not in extendedList and not node.isWall:
                    path.append(node)
                    a.append(path.copy())  # Add to a
                    path.pop(-1)

            # Sort a
            if a:
                min = a[0][-1].distance(end)
                for i in range(len(a)):
                    d = a[i][-1].distance(end)
                    if d < min:
                        t = a[0]
                        a[0] = a[i]
                        a[i] = t
                        min = d
                for p in a[::-1]:
                    agenda.insert(0, p)

        for eve in event.get():
            if eve.type == QUIT:
                sys.exit()
            if eve.type == KEYDOWN:
                if eve.key == K_h:
                    return
        # Draw the current node (green) + checked nodes(red)
        path[-1].isCurrent = True
        g.draw()
        path[-1].isCurrent = False
        path[-1].checked = True
        display.update()
    return(None)

def reset():
    g.reset(True)

def quit():
    sys.exit()

def findPath(start, end):
    HillClimb(start, end)

def movePeople():
    people = findPeople
    


def findPeople():
    people = []
    for i in range(g.x_elems):
        for j in range(g.y_elems):
            if(g.grid[i][j].isPerson):
                people.append(g.grid[i][j])
    return people


funcs = {K_BACKSPACE: reset, K_a: findPath, K_ESCAPE: quit}

start = (0,0)
end = (g.x_elems - 1, g.y_elems - 1)






while True:
    g.grid[start[1]][start[0]].isStart = True
    g.grid[start[1]][start[0]].isWall = False
    g.grid[end[1]][end[0]].isEnd = True
    g.grid[end[1]][end[0]].isWall = False

    g.draw()
    for eve in event.get():
        if eve.type == QUIT:
            sys.exit()
        if eve.type == KEYDOWN:
            mousePos = mouse.get_pos()
            if eve.key in funcs.keys():
                if not eve.key in [K_BACKSPACE, K_g]:
                    funcs[eve.key](start, end)
                else:
                    funcs[eve.key]()
            if eve.key == K_s:
                g.grid[start[1]][start[0]].isStart = False
                start = ((mousePos[0] // g.n_width), (mousePos[1] // g.n_width))
            if eve.key == K_e:
                g.grid[end[1]][end[0]].isEnd = False
                end = ((mousePos[0] // g.n_width), (mousePos[1] // g.n_width))
    movePeople()
    display.update()
