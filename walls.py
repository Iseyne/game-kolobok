import config
import zone

class Wall:
    def __init__(self, width, height, x, y):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__zone = zone.Zone(self.__x, self.__y, self.__x + self.__width, self.__y, self.__x + self.__width, self.__y + self.__height, self.__x, self.__y + self.__height)
        
    def get_zone(self):
        return self.__zone

class Walls:
    
    def __init__(self):
        self.__walls = [
            Wall(config.wall_width_1, config.wall_height_1, config.wall_x_1, config.wall_y_1),
            Wall(config.wall_width_2, config.wall_height_2, config.wall_x_2, config.wall_y_2),
            Wall(config.wall_width_3, config.wall_height_3, config.wall_x_3, config.wall_y_3),
            Wall(config.wall_width_4, config.wall_height_4, config.wall_x_4, config.wall_y_4),
            Wall(config.wall_width_5, config.wall_height_5, config.wall_x_5, config.wall_y_5)
        ]
        
    def get_zone(self):
        zones = []
        for i in self.__walls:
            zones.append(i.get_zone())
        return zones