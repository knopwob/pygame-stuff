#!/usr/bin/env python2

import pygame
import sys
import random

from knopgame.vector2d import Vector2D

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
        return self.pos.y > height

class Glimmer(Particle):
    def __init__(self, pos, vel=Vector2D(0,0)):
        Particle.__init__(self, pos, vel)

    def update(self):
        Particle.update(self)
        self.fade_color()

    def fade_color(self):
        (r,g,b) = self.color
        r = max(0, r - 3)
        g = max(0, g - 3)
        b = max(0, b - 3)
        self.color = (r,g,b)


class Firework(Particle):
    def __init__(self):
        pos = Vector2D(random.randint(0, width), height)
        vel_x = random.randint(-2, 2)
        vel_y = -1 * random.randint(8, 12)
        vel = Vector2D(vel_x, vel_y)
        Particle.__init__(self, pos, vel)

        r = random.randint(100,255)
        g = random.randint(100,255)
        b = random.randint(100,255)
        self.color = (r,g,b)
        self.exploded = False

    def explode(self):
        self.exploded = True
        print "exploding"
        global objects
        for i in xrange(0,60):
            vx = random.uniform(-4,4) + self.vel.x
            vy = random.uniform(-4,3)
            v = Vector2D(vx,vy)
            p = Glimmer(self.pos.copy(), v)
            p.color = self.color
            p.r = 1
            objects.append(p)


    def update(self):
        Particle.update(self)
        if self.vel.y >= 0 and not self.exploded:
            self.explode()

    def alive(self):
        return  self.exploded

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

    if random.randint(1, 20) == 1:
        f = Firework()
        objects.append(f)

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
