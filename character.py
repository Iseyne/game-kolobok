import config, quest, pygame

class Character:

    def __init__(self, spec):
        self.__name = spec["name"]
        self.__width = config.width // spec["width_ratio"]
        self.__height = config.bg_height // spec["height_ratio"]
        self.__x = spec["x"]
        self.__y = spec["y"]
        self.__sprite = None
        if spec["sprite"] is not None:
            self.__sprite = pygame.transform.smoothscale(pygame.image.load(spec["sprite"]).convert_alpha(), (self.__width, self.__height))
            if spec["rotate"]:
                self.__sprite = pygame.transform.rotate(self.__sprite, spec["rotate"])
        self.__quest = quest.Quest(False, spec["task_text"], spec["result_text"], spec["required_items"])
        self.__item = spec["reward"]
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

    @property
    def name(self):
        return self.__name

    def get_rect(self):
        return self.__rect

    def draw(self, screen):
        if self.__sprite is not None:
            screen.blit(self.__sprite, (self.__x, self.__y))

    def show_text(self, inventory):
        return self.__quest.get_text(inventory, self.__item)