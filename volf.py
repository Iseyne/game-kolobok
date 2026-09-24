import config, quest, pygame 


class Volf:
    def __init__(self):
        self.__width = config.width // 13
        self.__height = config.bg_height // 7
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.volf_image).convert_alpha(), (self.__width, self.__height))
        self.__x = config.volf_x
        self.__y = config.volf_y
        self.__quest = quest.Quest(False, config.volf_task_text, config.volf_result_text, config.volf_item)
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))      
        self.__item = "морковь"
        
    def get_rect(self):
        return self.__rect
        
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))
        
    def show_text(self, inventory): 
        return self.__quest.get_text(inventory, self.__item)    