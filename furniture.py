import pygame

class Furniture:
    def __init__(self, x, y, width, height, task, sprite):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__task = task
        self.__sprite = None
        if sprite is not None:
            self.__sprite = pygame.transform.smoothscale(pygame.image.load(sprite).convert_alpha(), (self.__width, self.__height))
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

    @property
    def task(self):
        return self.__task

    def get_rect(self):
        return self.__rect

    def draw(self, screen):
        if self.__sprite is not None:
            screen.blit(self.__sprite, (self.__x, self.__y))