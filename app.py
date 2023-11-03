import pygame
import config
import kolobok
import medved
import volf
import rabbit
import fox
import walls
import furniture
import zone

             

class Game:
    # Конструктор
    def __init__(self):
        pygame.init()
        
        # Настройки игрового окна
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.bg).convert_alpha(), (self.__width, self.__height))
        self.__fps = config.fps
        self.__clock = pygame.time.Clock()
        
        # Флаг конца игры
        self.__game_end = False
        self.__player = kolobok.Kolobok()
        self.__medved = medved.Medved()
        self.__volf = volf.Volf()
        self.__rabbit = rabbit.Rabbit()
        self.__fox = fox.Fox()
        self.__walls = walls.Walls() 
        self.__safe = furniture.Furniture(config.safe_width, config.safe_height, config.safe_x, config.safe_y, config.safe_image)
        self.__cabinet_1 = furniture.Furniture(config.cabinet_width_1, config.cabinet_height_1, config.cabinet_x_1, config.cabinet_y_1, config.cabinet_image)
        self.__cabinet_2 = furniture.Furniture(config.cabinet_width_2, config.cabinet_height_2, config.cabinet_x_2, config.cabinet_y_2, config.cabinet_image)
        self.__bake = furniture.Furniture(config.bake_width, config.bake_height, config.bake_x, config.bake_y, config.bake_image)
        self.__fridge = furniture.Furniture(config.fridge_width, config.fridge_height, config.fridge_x, config.fridge_y, config.fridge_image)
        
        self.__restricted_zones = self.__fill_restricted_zones()
        
    def __fill_restricted_zones(self):
        return [self.__medved.get_zone(),
                self.__volf.get_zone(),
                self.__rabbit.get_zone(),
                self.__fox.get_zone(),
                *self.__walls.get_zone(),
                self.__safe.get_zone(),
                self.__cabinet_1.get_zone(),
                self.__cabinet_2.get_zone(),
                self.__bake.get_zone(),
                self.__fridge.get_zone()
            ]
        
    # Деструктор
    def __del__(self):
        pygame.quit()
    
    # Игровой цикл
    def run(self):
        while not self.__game_end: # Пока игра не завершена
            self.__check_events() # Проверка событий
            self.__move_objects() # Движение объектов на экране
            self.__check_logic() # Проверка логики игры
            
            self.__draw() # Отрисовка экрана

            self.__clock.tick(self.__fps) # Контроль FPS
            
    # Проверка событий   
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__game_end = True
            elif event.type == pygame.QUIT:
                self.__game_end = True
                
            self.__player.check_event(event)
    # Проверка логики игры
    def __check_logic(self):
        self.__player.check_logic(self.__width, self.__height)

    # Движение объектов на экране
    def __move_objects(self):
        self.__player.move(self.__restricted_zones)

    # Отрисовка экрана
    def __draw(self):
        self.__screen.blit(self.__bg, (0, 0)) # Заливаем экран
        self.__player.draw(self.__screen)
        self.__medved.draw(self.__screen)
        self.__volf.draw(self.__screen)
        self.__rabbit.draw(self.__screen)
        self.__fox.draw(self.__screen)
        self.__safe.draw(self.__screen)
        self.__cabinet_1.draw(self.__screen)
        self.__cabinet_2.draw(self.__screen)
        self.__bake.draw(self.__screen)
        self.__fridge.draw(self.__screen)
        
        pygame.display.flip() # Показываем экран пользователю
        
