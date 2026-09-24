import pygame, config, time

class Cabinet_task:
    def __init__(self, inventory):
        pygame.init()
        pygame.font.init()
        
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.cabinet_task_image).convert_alpha(), (self.__width, config.bg_height))        
        
        self.__font = pygame.font.Font(None, 30)
        self.__text = self.__font.render(config.cabinet_task_text, True, config.text_color)
        self.__text_false = self.__font.render("НЕВЕРНО!", True, (255, 0, 0))
        self.__text_true = self.__font.render("ВЕРНО!", True, (0, 255, 0))
        self.__text_one = self.__font.render(config.cabinet_task_text_one, True, config.text_color)
        self.__text_two = self.__font.render(config.cabinet_task_text_two, True, config.text_color)
        self.__text_three = self.__font.render(config.cabinet_task_text_three, True, config.text_color)
        self.__text_four = self.__font.render(config.cabinet_task_text_four, True, config.text_color)
        
        self.__screen.blit(self.__bg, (0, 0))
        self.__screen.blit(self.__text, (config.text_x, config.text_y - 15))
        self.__screen.blit(self.__text_one, (config.text_x, config.text_y + 25))
        self.__screen.blit(self.__text_two, (config.text_x + 350, config.text_y + 25))
        self.__screen.blit(self.__text_three, (config.text_x, config.text_y + 75))
        self.__screen.blit(self.__text_four, (config.text_x + 350, config.text_y + 75))   
        
        pygame.display.flip()        
        
        self.__answer = False
        while self.__answer == False:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.__answer = 1
                    elif event.key == pygame.K_2:
                        self.__answer = 2  
                    elif event.key == pygame.K_3:
                        self.__answer = 3 
                    elif event.key == pygame.K_4:
                        self.__answer = 4 
                        
                    
        
        if self.__answer != 4:
            self.__screen.blit(self.__text_false, (config.text_x + 500, config.text_y - 15))
            pygame.display.flip()
        else:
            self.__screen.blit(self.__text_true, (config.text_x + 500, config.text_y - 15))
            pygame.display.flip()  
            inventory.add("ключ")
            
        time.sleep(3)
        
