import config, quest, pygame

class Rabbit:
    def __init__(self):
        self.__width = config.width // 10
        self.__height = config.bg_height // 7
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.rabbit_image).convert_alpha(), (self.__width, self.__height))
        self.__sprite = pygame.transform.rotate(self.__sprite, 90)
        self.__x = config.rabbit_x
        self.__y = config.rabbit_y
        self.__quest = quest.Quest(False, config.rabbit_task_text, config.rabbit_result_text, config.rabbit_item)
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        self.__item = "код от сейфа"
    
    def get_rect(self):
        return self.__rect
        
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))      
        
    def show_text(self, inventory):
        return self.__quest.get_text(inventory, self.__item)