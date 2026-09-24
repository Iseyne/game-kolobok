import pygame, time, config

class Finish_task:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height)) 
        
        self.__font = pygame.font.Font(None, 45)
        self.__text = self.__font.render("Спасибо, что прошёл мою игру))", True, config.text_color)        
        
        self.__screen.fill((0, 0, 0))
        self.__screen.blit(self.__text, (150, 275))   
        
        pygame.display.flip()
        
        time.sleep(5)
        