import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

width = 1760
height = 990
random.seed(10)

def star_point():
    x = random.randint(0, width)
    y = random.randint(0, height)
    z = random.randint(0,4)
    return (x, y, z)

def draw_star(star_arr):
    glPointSize(1.0)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex3f(star_arr[0], star_arr[1], star_arr[2])
    glEnd()

def update_star(star_arr,pos):
    x = (star_arr[0] - width/2)*pos *0.00001 + star_arr[0]
    y = (star_arr[1] - height/2)*pos*0.00001 + star_arr[1] 
    z = star_arr[2]
    draw_star([x,y,z])
    return [x,y,z]

def main():
    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glViewport(0, 0, width, height)
    gluOrtho2D(0, width, height, 0)

    pos = 0
    stars = []
    for _ in range(height):
        star = star_point()
        stars.append(star)
        draw_star(star)

    while True:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for index, star in enumerate(stars):
            new_star_pos = update_star(star,pos)
            if new_star_pos[0] < 0 or new_star_pos[0] > width or new_star_pos[1] < 0 or new_star_pos[1] > height:
                stars[index] = star_point()
            else:
                stars[index] = new_star_pos

        pygame.display.flip()
        pygame.time.wait(1)

        new_pos = pygame.mouse.get_pos()[0]

        if pos != new_pos: 
            pos = new_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
main()
