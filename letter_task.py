import pygame, config, time

class Letter_task:
    def __init__(self):
        pygame.init()
        
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.letter_image).convert_alpha(), (self.__width, self.__height))        
        
    
        self.__screen.blit(self.__bg, (0, 0))
        pygame.display.flip()
        
        time.sleep(3)
        