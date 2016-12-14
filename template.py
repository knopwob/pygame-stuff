#!/usr/bin/env python2

import pygame
import sys

##############################
# CLASSES
##############################

class Particle(object):
    def __init__(self, pos, vel=Vector2D(0,0)):
        self.pos = pos
        self.vel = vel
        self.acc = Vector2D(0, 0)
        self.color = COLOR_WHITE
        self.r = 2

    def apply_force(self, force):
        self.vel.add(force)

    def draw(self):
        p = map(int, self.pos.as_tuple())
        pygame.draw.circle(screen, self.color, p, self.r, 0)

    def update(self):
        self.apply_force(gravity)
        self.pos.add(self.vel)

    def alive(self):
        return self.pos.x < 0 or self.pos.x > width or self.pos.y < 0 or self.pos.y > height


##############################
# GLOBALS
##############################

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)

width = 800
height = 600

screen = None
clock = None
elapsed = 0

gravity = Vector2D(0, 0.2)

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

def loop():
    global objects
    global elapsed

    keep_running = True
    elapsed = clock.tick(60)

    screen.fill(COLOR_BLACK)
    for o in objects:
        o.update()
        o.draw()

    # remove deleteable particles
    objects = filter(lambda x: not x.alive(), objects)
    print len(objects)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False
    return keep_running

def main():
    setup()

    while(loop()):
        pass

    print "exiting cleanly"

if __name__ == "__main__":
    main()
