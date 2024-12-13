import math


def add(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    if float(b) == 0:
        return float(a) / float(b)


def circle(radius):
        r = float(radius)
        if r <= 0:
            raise TypeError
        return math.pi * r * r

def square(side):
        s = float(side)
        if s <= 0:
            raise TypeError
        return s * s


def rectangle(length, width):
        l = float(length)
        w = float(width)
        if l <= 0 or w <= 0:
            raise TypeError
        return l * w

def triangle(base, height):
        b = float(base)
        h = float(height)
        if b <= 0 or h <= 0:
            raise TypeError
        return 0.5 * b * h
