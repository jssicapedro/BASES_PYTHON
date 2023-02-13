""" Programa que abra e reproduza o áudio de um arquivo mp3. """
import pygame
pygame.init()
pygame.mixer.music.load('d022-aula6.mp3')
pygame.mixer.music.play()
pygame.event.waint()