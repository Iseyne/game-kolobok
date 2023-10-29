import pygame
import config

class Kolobok:
    def __init__(self):
        self.__width = config.width // 14
        self.__height = config.height // 10
        self.__sprite = pygame.transform.smoothscale(pygame.image.load(config.kolobok_image).convert_alpha(),(self.__width, self.__height))
        self.__x = config.kolobok_x
        self.__y = config.kolobok_y
    def draw(self, screen):
        screen.blit(self.__sprite, (self.__x, self.__y))
class Game:
    # Конструктор
    def __init__(self):
        pygame.init()
        
        # Настройки игрового окна
        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.bg).convert_alpha(),(self.__width, self.__height))
        self.__fps = config.fps
        self.__clock = pygame.time.Clock()
        # Флаг конца игры
        self.__game_end = False
        self.__player = Kolobok()
        
    # Деструктор
    def __del__(self):
        pygame.quit()
    
    # Игровой цикл
    def run(self):
        while not self.__game_end: # Пока игра не завершена
            self.__check_events() # Проверка событий
            self.__check_logic() # Проверка логики игры
            self.__move_objects() # Движение объектов на экране
            self.__draw() # Отрисовка экрана

            self.__clock.tick(self.__fps) # Контроль FPS
            
    # Проверка событий   
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__game_end = True

    # Проверка логики игры
    def __check_logic(self):
        pass

    # Движение объектов на экране
    def __move_objects(self):
        pass
    # Отрисовка экрана
    def __draw(self):
        self.__screen.blit(self.__bg, (0, 0)) # Заливаем экран
        self.__player.draw(self.__screen)
        pygame.display.flip() # Показываем экран пользователю
        


def main():
    game = Game() # Создаём объеки класса Game
    game.run() # Запускаем игру

# Проверка на то, что файл запущен, как исполняемый
if __name__ == "__main__":
    main()