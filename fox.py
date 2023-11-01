import config
import zone
import pygame


class Fox:
    def __init__(self):
        self.__width = config.width // 15
        self.__height = config.height // 7
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.fox_image).convert_alpha(), (self.__width, self.__height))
        self.__x = config.fox_x
        self.__y = config.fox_y
        self.__zone = zone.Zone(self.__x, self.__y, self.__x + self.__width, self.__y, self.__x + self.__width, self.__y + self.__height, self.__x, self.__y + self.__height)
        
    def get_zone(self):
        return self.__zone
        
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))