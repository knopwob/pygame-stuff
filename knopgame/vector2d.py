#!/usr/bin/env python2

class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def copy(self):
        return Vector2D(self.x, self.y)

    def equals(self, other):
        return self.x == other.x and self.y == other.y
