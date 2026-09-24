import pygame, config, time

class Bake_task:
    def __init__(self, inventory):
        pygame.init()
        pygame.font.init()
        
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.bake_task_image).convert_alpha(), (self.__width, config.bg_height))        
        
        self.__font = pygame.font.Font(None, 30)
        self.__text = self.__font.render(config.bake_task_text, True, config.text_color)
        self.__text_one = self.__font.render(config.bake_task_text_one, True, config.text_color)
        self.__text_two = self.__font.render(config.bake_task_text_two, True, config.text_color)
        self.__text_true = self.__font.render("Вы взяли муку!", True, (0, 255, 0))
        
        
        
        self.__screen.blit(self.__bg, (0, 0))
        self.__screen.blit(self.__text, (config.text_x, config.text_y - 15))
        self.__screen.blit(self.__text_one, (config.text_x, config.text_y + 25))
        self.__screen.blit(self.__text_two, (config.text_x + 350, config.text_y + 25))

        
        pygame.display.flip()        
        
        self.__answer = False
        while self.__answer == False:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.__answer = 1
                    elif event.key == pygame.K_2:
                        self.__answer = 2  
                    
                        
                    
        
        if self.__answer == 1:
            self.__screen.blit(self.__text_true, (config.text_x, config.text_y + 50))
            pygame.display.flip()  
            inventory.add("мука")
            
            time.sleep(3)
