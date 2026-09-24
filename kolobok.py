import config, pygame

class Kolobok:

    def __init__(self, sprite=config.kolobok_image, x=config.kolobok_x, y=config.kolobok_y):
        self.__width = config.width // 14
        self.__height = config.bg_height // 10
        self.__sprite = None
        if sprite is not None:
            self.__sprite = pygame.transform.smoothscale(pygame.image.load(sprite).convert_alpha(), (self.__width, self.__height))
        self.__x = x
        self.__y = y
        self.__horizontal_move_flag = config.h_m_f
        self.__vertical_move_flag = config.v_m_f
        self.__speed = config.speed
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.__horizontal_move_flag = -1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.__horizontal_move_flag = 1
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                self.__vertical_move_flag = -1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.__vertical_move_flag = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.__horizontal_move_flag = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.__vertical_move_flag = 0

    def check_logic(self):
        if self.__x < config.boundary_left:
            self.__x = config.boundary_left
        elif self.__x > config.boundary_right:
            self.__x = config.boundary_right
        if self.__y < config.boundary_top:
            self.__y = config.boundary_top
        elif self.__y > config.boundary_bottom:
            self.__y = config.boundary_bottom

    def __calc_move_x(self):
        return self.__x + self.__speed * self.__horizontal_move_flag

    def __calc_move_y(self):
        return self.__y + self.__speed * self.__vertical_move_flag

    def move(self, restricted_zones):
        x = self.__calc_move_x()
        y = self.__calc_move_y()
        self.__rect = pygame.Rect((x, y), (self.__width, self.__height))
        if not self.__is_in_restricted_zone(restricted_zones):
            self.__x = x
            self.__y = y

    def get_zone(self):
        return self.__rect

    def draw(self, screen):
        if self.__sprite is not None:
            screen.blit(self.__sprite, (self.__x, self.__y))

    def __is_in_restricted_zone(self, restricted_zones):
        for i in range(len(restricted_zones)):
            if self.__rect.colliderect(restricted_zones[i]):
                return True
        return False

    def in_restricted_zone(self, restricted_zones):
        return self.__is_in_restricted_zone(restricted_zones)

    def index_restricted_zone(self, restricted_zones):
        for i in range(len(restricted_zones)):
            if self.__rect.colliderect(restricted_zones[i]):
                return i