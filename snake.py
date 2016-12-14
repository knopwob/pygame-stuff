#!/usr/bin/env python2

import pygame
import random
import sys

from knopgame.vector2d import Vector2D

##############################
# CLASSES
##############################

class GridObject(object):
    def __init__(self, pos):
        self.pos = pos
        self.color = COLOR_WHITE

    def draw(self):
        pygame.draw.rect(screen, self.color,
                (self.pos.x * 10,
                 self.pos.y * 10,
                 10, 10), 0)

class Food(GridObject):
    def __init__(self, pos):
        self.pos = pos
        self.color = COLOR_RED

    def update(self):
        pass

    def alive(self):
        return True

    def new_position(self):
        self.pos = Vector2D(random.randint(0, width/grid_size),
        random.randint(0, height/grid_size))

class Head(GridObject):
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector2D(0, -1)
        self.color = COLOR_WHITE

    def update(self):
        self.pos.add(self.vel)

    def alive(self):
        return True

    def left(self):
        self.vel = Vector2D(-1, 0)

    def right(self):
        self.vel = Vector2D(1, 0)

    def up(self):
        self.vel = Vector2D(0,-1)

    def down(self):
        self.vel = Vector2D(0, 1)

    def eat(self):
        print "eating"

##############################
# GLOBALS
##############################

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_RED = (220, 0, 0)

width  = 400
height = 400

grid_size = 10

screen = None
clock = None
elapsed = 0

gravity = Vector2D(0, 0.2)

head = None
food = None
objects = list()

##############################
# FUNCTIONS
##############################

def setup():
    pygame.init()

    global clock
    clock = pygame.time.Clock()

    global screen
    screen = pygame.display.set_mode((width, height))

    global objects
    global head
    global food
    head = Head(Vector2D(20, 20))
    food = Food(Vector2D(0,0))
    food.new_position()
    objects.append(head)
    objects.append(food)

def loop():
    global objects
    global elapsed

    keep_running = True
    elapsed = clock.tick(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                head.left()
            if event.key == pygame.K_RIGHT:
                head.right()
            if event.key == pygame.K_UP:
                head.up()
            if event.key == pygame.K_DOWN:
                head.down()

    screen.fill(COLOR_BLACK)
    if head.pos.equals(food.pos):
        head.eat()
        food.new_position()

    for o in objects:
        o.update()
        o.draw()

    # remove deleteable particles
    objects = filter(lambda x: x.alive(), objects)
    print len(objects)

    pygame.display.update()

    return keep_running

def main():
    setup()

    while(loop()):
        pass

    print "exiting cleanly"

if __name__ == "__main__":
    main()
