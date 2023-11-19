import config, quest, pygame


class Fox:
    def __init__(self):
        self.__width = config.width // 15
        self.__height = config.bg_height // 7
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.fox_image).convert_alpha(), (self.__width, self.__height))
        self.__x = config.fox_x
        self.__y = config.fox_y
        self.__quest = quest.Quest(False, config.fox_task_text, config.fox_result_text, config.fox_item)
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        self.__item = "отпечаток"
        
    def get_rect(self):
        return self.__rect
        
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))
        
    def show_text(self, inventory):
        return self.__quest.get_text(inventory, self.__item)    