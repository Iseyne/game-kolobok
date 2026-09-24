import config, pygame

class Wall:
    def __init__(self, width, height, x, y):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

    def get_rect(self):
        return self.__rect

class Walls:
    def __init__(self):
        self.__walls = [Wall(wall["width"], wall["height"], wall["x"], wall["y"]) for wall in config.WALLS]

    def get_rect(self):
        return [wall.get_rect() for wall in self.__walls]