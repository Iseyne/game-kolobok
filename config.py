# Настройки экрана

width = 800
height = 800
bg_color = (0, 0, 0)
fps = 60
bg = "sprites/bg.png"
bg_height = 600
text_none = ''
text_color = (255, 255, 255)
text_x = 50
text_y = 650

# Настройки колобка

kolobok_x = 200
kolobok_y = 100
h_m_f = 0
v_m_f = 0
speed = 3
kolobok_image = "sprites/kolobok.png"

# Границы игрового поля

boundary_left = 37
boundary_right = 705
boundary_top = 37
boundary_bottom = 500

# Стены (каждая запись — прямоугольник)

WALLS = [
    {"width": 570, "height": 7, "x": 37, "y": 297},
    {"width": 100, "height": 7, "x": 700, "y": 297},
    {"width": 10, "height": 80, "x": 400, "y": 50},
    {"width": 10, "height": 180, "x": 400, "y": 225},
    {"width": 10, "height": 100, "x": 400, "y": 525},
]

# Неигровые персонажи: спрайт, размер, позиция и квест.

# Порядок важен: он совпадает с порядком зон взаимодействия (NPC идут первыми).

NPC_DEFS = [
    {
        "name": "rabbit",
        "sprite": "sprites/rabbit.png",
        "x": 50,
        "y": 200,
        "width_ratio": 10,
        "height_ratio": 7,
        "rotate": 90,
        "task_text": "Принеси сюда морковный торт и получишь код!",
        "result_text": "Спасибо за торт! Вот тебе код, как и обещал!",
        "required_items": {"торт"},
        "reward": "код от сейфа",
    },
    {
        "name": "medved",
        "sprite": "sprites/medved.png",
        "x": 675,
        "y": 475,
        "width_ratio": 10,
        "height_ratio": 7,
        "rotate": -90,
        "task_text": "Принеси мне морковь, молоко, муку, яйца. Будет тебе торт.",
        "result_text": "Вот твой торт!",
        "required_items": {"мука", "яйца", "морковь", "молоко"},
        "reward": "торт",
    },
    {
        "name": "volf",
        "sprite": "sprites/volf.png",
        "x": 700,
        "y": 50,
        "width_ratio": 13,
        "height_ratio": 7,
        "rotate": 0,
        "task_text": "",
        "result_text": "Нужна морковка? На держи!",
        "required_items": set(),
        "reward": "морковь",
    },
    {
        "name": "fox",
        "sprite": "sprites/fox.png",
        "x": 325,
        "y": 325,
        "width_ratio": 15,
        "height_ratio": 7,
        "rotate": 0,
        "task_text": "Чтобы получить отпечаток, выиграй меня.",
        "result_text": "О нет, ты победил!",
        "required_items": {"МЕЧ"},
        "reward": "отпечаток",
    },
]

# Мебель: позиция, размер, спрайт и связанное задание (ключ в tasks.TASK_SPECS).

FURNITURE = [
    {"sprite": "sprites/safe.png", "x": 37, "y": 37, "width": 75, "height": 80, "task": "safe"},
    {"sprite": "sprites/cabinet.png", "x": 325, "y": 37, "width": 75, "height": 80, "task": "cabinet"},
    {"sprite": "sprites/cabinet.png", "x": 410, "y": 305, "width": 75, "height": 80, "task": "letter"},
    {"sprite": "sprites/bake.png", "x": 450, "y": 500, "width": 125, "height": 60, "task": "bake"},
    {"sprite": "sprites/fridge.png", "x": 410, "y": 37, "width": 75, "height": 90, "task": "fridge"},
    {"sprite": "sprites/painting.png", "x": 410, "y": 281, "width": 115, "height": 15, "task": "painting"},
    {"sprite": "sprites/exit.png", "x": 150, "y": 560, "width": 75, "height": 35, "task": "exit"},
    {"sprite": "sprites/table.png", "x": 37, "y": 325, "width": 75, "height": 135, "task": "table"},
]