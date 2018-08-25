#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:34:39 2018

@author: kay
"""

import pygame
import sys
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Sample Pygame')
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
            quit()
        print(event)
    pygame.display.update()
    clock.tick(60)

