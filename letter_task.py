import pygame, config

class Letter_task:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.letter_task_image).convert_alpha(), (self.__width, config.bg_height))        
        
        self.__font = pygame.font.Font(None, 30)
        self.__text = self.__font.render(config.letter_task_text, True, config.text_color)        
        self.__text_one = self.__font.render(config.letter_task_text_one, True, config.text_color)
        
        self.__screen.blit(self.__bg, (0, 0))
        self.__screen.blit(self.__text, (config.text_x, config.text_y - 15))
        self.__screen.blit(self.__text_one, (config.text_x, config.text_y + 25))   
        
        pygame.display.flip()
        
        self.__answer = False
        while self.__answer == False:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.__answer = True        