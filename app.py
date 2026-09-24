import pygame, config, kolobok, character, furniture, walls
import tasks
from task_base import TaskScene

FINISH_KEY = "КОНЕЦ"


def is_game_finished(inventory):
    return FINISH_KEY in inventory


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.__width = config.width
        self.__height = config.height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.transform.smoothscale(pygame.image.load(config.bg).convert_alpha(), (self.__width, config.bg_height))
        self.__fps = config.fps
        self.__clock = pygame.time.Clock()

        self.__game_end = False

        self.__player = kolobok.Kolobok()
        self.__characters = [character.Character(spec) for spec in config.NPC_DEFS]
        self.__furniture = [furniture.Furniture(spec["x"], spec["y"], spec["width"], spec["height"], spec["task"], spec["sprite"]) for spec in config.FURNITURE]
        self.__walls = walls.Walls()
        self.__restricted_zones = self.__rects()

        self.__inventory = set()
        self.__nps_texts = self.__characters
        self.__nps_text_index = None
        self.__text = None
        self.__font = pygame.font.Font(None, 30)
        self.__counter = 0

    def __rects(self):
        return [character.get_rect() for character in self.__characters] + \
               [furniture.get_rect() for furniture in self.__furniture] + \
               self.__walls.get_rect()

    def __del__(self):
        pygame.quit()

    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__move_objects()
            self.__check_logic()

            self.__draw()

            self.__clock.tick(self.__fps)

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__counter = 0

                elif event.key == pygame.K_i:
                    self.__counter = 2

                elif event.key == pygame.K_e:
                    zone_index = self.__player.index_restricted_zone(self.__restricted_zones)
                    if zone_index is None:
                        pass
                    elif zone_index < len(self.__nps_texts):
                        self.__counter = 1
                        self.__nps_text_index = zone_index
                    else:
                        furniture_index = zone_index - len(self.__nps_texts)
                        if furniture_index < len(self.__furniture):
                            task_key = self.__furniture[furniture_index].task
                            TaskScene(tasks.TASK_SPECS[task_key]).run(self.__inventory)

            elif event.type == pygame.QUIT:
                self.__game_end = True

            self.__player.check_event(event)

    def __check_logic(self):
        self.__player.check_logic()

        if is_game_finished(self.__inventory):
            TaskScene(tasks.TASK_SPECS["finish"]).run(self.__inventory)
            self.__game_end = True

        if self.__counter == 0:
            self.__text = self.__font.render(config.text_none, True, config.text_color)
        elif self.__counter == 1:
            self.__text = self.__font.render(self.__nps_texts[self.__nps_text_index].show_text(self.__inventory), True, config.text_color)
        elif self.__counter == 2:
            if self.__inventory == set():
                self.__text = self.__font.render("Пусто", True, config.text_color)
            else:
                word = "Вещи: "
                for i in self.__inventory:
                    word += i + ", "
                self.__text = self.__font.render(word, True, config.text_color)

    def __move_objects(self):
        self.__player.move(self.__restricted_zones)

    def __draw(self):
        self.__screen.fill(config.bg_color)
        self.__screen.blit(self.__bg, (0, 0))
        self.__screen.blit(self.__text, (config.text_x, config.text_y))
        self.__player.draw(self.__screen)
        for sprite in self.__characters:
            sprite.draw(self.__screen)
        for sprite in self.__furniture:
            sprite.draw(self.__screen)

        pygame.display.flip()