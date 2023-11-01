import config
import zone
import pygame


class Kolobok:
    
    def __init__(self):
        self.__width = config.width // 14
        self.__height = config.height // 10
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.kolobok_image).convert_alpha(), (self.__width, self.__height))
        self.__x = config.kolobok_x
        self.__y = config.kolobok_y
        self.__horizontal_move_flag = config.h_m_f
        self.__vertical_move_flag = config.v_m_f
        self.__speed = config.speed
                
        
    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.__horizontal_move_flag = -1
            elif event.key == pygame.K_d:
                self.__horizontal_move_flag = 1
            elif event.key == pygame.K_w:
                self.__vertical_move_flag = -1
            elif event.key == pygame.K_s:
                self.__vertical_move_flag = 1  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                self.__horizontal_move_flag = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                self.__vertical_move_flag = 0           
                
    def check_logic(self, screen_width, screen_height):
        if self.__x  < 37:
            self.__x = 37
        elif self.__x > 705:
            self.__x = 705 
        if self.__y < 37:
            self.__y = 37
        elif self.__y > 500:
            self.__y = 500
            
    def __calc_move_x(self):
        return self.__x + self.__speed * self.__horizontal_move_flag
    
    def __calc_move_y(self):
        return self.__y + self.__speed * self.__vertical_move_flag    
    
    def move(self, restricted_zones):
        x = self.__calc_move_x()
        y = self.__calc_move_y()
        self.__zone = zone.Zone(x, y, x + self.__width, y, x + self.__width, y + self.__height, x, y + self.__height).get_list()
        if not self.__is_in_restricted_zone(restricted_zones):
            self.__x = x
            self.__y = y
    
    def get_zone(self):
        return self.__zone
            
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))
        
    def __is_in_restricted_zone(self, restricted_zones):
        for i in range(len(restricted_zones)):
            if restricted_zones[i].is_in_zone(self.__zone):
                return True
        return False
                 
