import config, pygame  

class Furniture:
    
    def __init__(self, width, height, x, y, sprite):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(sprite).convert_alpha(), (self.__width, self.__height))
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))
        
    def get_rect(self):
        return self.__rect
    
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))    
