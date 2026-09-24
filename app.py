import pygame, config, kolobok, medved, volf, rabbit, fox, walls, furniture
import letter_task, painting_task, bake_task, cabinet_task, fridge_task, safe_task, exit_task, table_task, finish_task
             

class Game:
    # Конструктор
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        # Настройки игрового окна
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.bg).convert_alpha(), (self.__width, config.bg_height))
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
        self.__safe = furniture.Furniture(config.safe_width,
                                          config.safe_height,
                                          config.safe_x,
                                          config.safe_y,
                                          config.safe_image
                                          )
        self.__cabinet_1 = furniture.Furniture(config.cabinet_width_1,
                                               config.cabinet_height_1,
                                               config.cabinet_x_1,
                                               config.cabinet_y_1,
                                               config.cabinet_image
                                               )
        self.__cabinet_2 = furniture.Furniture(config.cabinet_width_2,
                                               config.cabinet_height_2,
                                               config.cabinet_x_2,
                                               config.cabinet_y_2,
                                               config.cabinet_image
                                               )
        self.__bake = furniture.Furniture(config.bake_width,
                                          config.bake_height,
                                          config.bake_x,
                                          config.bake_y,
                                          config.bake_image
                                          )
        self.__fridge = furniture.Furniture(config.fridge_width,
                                            config.fridge_height,
                                            config.fridge_x,
                                            config.fridge_y,
                                            config.fridge_image
                                            )
        self.__painting = furniture.Furniture(config.painting_width,
                                              config.painting_height,
                                              config.painting_x,
                                              config.painting_y,
                                              config.painting_image
                                              )
        
        self.__exit = furniture.Furniture(config.exit_width,
                                              config.exit_height,
                                              config.exit_x,
                                              config.exit_y,
                                              config.exit_image
                                              )        
        
        self.__table = furniture.Furniture(config.table_width,
                                              config.table_height,
                                              config.table_x,
                                              config.table_y,
                                              config.table_image
                                              )                
        
        self.__inventory = set()
        self.__restricted_zones = self.__rects()
        
        self.__nps_texts = [self.__rabbit, self.__medved, self.__volf, self.__fox]           
        self.__nps_text_index = None
        self.__text = None
        self.__font = pygame.font.Font(None, 30)
        self.__counter = 0
             
        
    def __rects(self):
        return [self.__rabbit.get_rect(), 
                self.__medved.get_rect(),
                self.__volf.get_rect(),
                self.__fox.get_rect(),
                self.__safe.get_rect(),
                self.__cabinet_1.get_rect(),
                self.__cabinet_2.get_rect(),
                self.__bake.get_rect(),
                self.__fridge.get_rect(),
                self.__painting.get_rect(),
                self.__exit.get_rect(),
                self.__table.get_rect(),
                *self.__walls.get_rect()
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
                    self.__counter = 0
                
                elif event.key == pygame.K_i:
                    self.__counter = 2
                    
                elif event.key == pygame.K_e and self.__player.in_restricted_zone(self.__restricted_zones) and self.__player.index_restricted_zone(self.__restricted_zones) < len(self.__nps_texts):
                    self.__counter = 1
                    self.__nps_text_index = self.__player.index_restricted_zone(self.__restricted_zones)
                    
                elif event.key == pygame.K_e and self.__player.in_restricted_zone(self.__restricted_zones) and self.__player.index_restricted_zone(self.__restricted_zones) >= len(self.__nps_texts): 
                    if self.__player.index_restricted_zone(self.__restricted_zones) == 4:
                        self.__safe_task = safe_task.Safe_task(self.__inventory)
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 5:
                        self.__cabinet_task = cabinet_task.Cabinet_task(self.__inventory)
                    
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 6:
                        self.__letter = letter_task.Letter_task()
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 7:
                        self.__bake_task = bake_task.Bake_task(self.__inventory)  
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 8:
                        self.__fridge_task = fridge_task.Fridge_task(self.__inventory)
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 9:
                        self.__painting_task = painting_task.Painting_task(self.__inventory)
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 10:
                        self.__exit_task = exit_task.Exit_task(self.__inventory)      
                        
                    elif self.__player.index_restricted_zone(self.__restricted_zones) == 11:
                        self.__table_task = table_task.Table_task(self.__inventory)                        
                        
            elif event.type == pygame.QUIT:
                self.__game_end = True
                
            elif self.__inventory | {"КОНЕЦ"} == self.__inventory:
                self.__finish_task = finish_task.Finish_task()
                self.__game_end = True
                
            self.__player.check_event(event)
    # Проверка логики игры
    def __check_logic(self):
        self.__player.check_logic(self.__width, self.__height)
        
        if self.__counter == 0:
            self.__text = self.__font.render(config.text_none, True, config.text_color)
        elif self.__counter == 1:             
            self.__text = self.__font.render(self.__nps_texts[self.__nps_text_index].show_text(self.__inventory), True, config.text_color)  
        elif self.__counter == 2:
            if self.__inventory == set():
                self.__text = self.__font.render("Пусто", True, config.text_color)
            else:
                self.__word = "Вещи: "
                for i in self.__inventory:
                    self.__word += i + ", "
                self.__text = self.__font.render(self.__word, True, config.text_color)

    # Движение объектов на экране
    def __move_objects(self):
        self.__player.move(self.__restricted_zones)
    
    # Отрисовка экрана
    def __draw(self):
        self.__screen.fill(config.bg_color)
        self.__screen.blit(self.__bg, (0, 0))
        self.__screen.blit(self.__text, (config.text_x, config.text_y))# Заливаем экран
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
        self.__painting.draw(self.__screen)
        self.__table.draw(self.__screen)
        self.__exit.draw(self.__screen)
        
        pygame.display.flip() # Показываем экран пользователю
        
