import time

import config, pygame


class TaskResult:
    def __init__(self, success, feedback=None, add_items=None, remove_items=None):
        self.success = success
        self.feedback = feedback
        self.add_items = add_items or set()
        self.remove_items = remove_items or set()


def evaluate(spec, inventory, choice):
    task_type = spec["type"]

    if task_type in ("note", "ending"):
        return TaskResult(success=True)

    if task_type == "quiz":
        if choice == spec["correct"]:
            return TaskResult(
                success=True,
                feedback=spec["feedback"]["success"],
                add_items=set(spec.get("add_items", [])),
            )
        return TaskResult(success=False, feedback=spec["feedback"]["fail"])

    if task_type == "take":
        if choice != 1:
            return TaskResult(success=False)
        required = set(spec.get("required", []))
        if required and not required <= inventory:
            return TaskResult(success=False, feedback=spec["feedback"]["fail"])
        return TaskResult(
            success=True,
            feedback=spec["feedback"]["success"],
            add_items=set(spec.get("add_items", [])),
            remove_items=set(spec.get("remove_items", [])),
        )

    raise ValueError("Unknown task type: %s" % task_type)


class TaskScene:

    def __init__(self, spec):
        self.__spec = spec
        self.__screen = pygame.display.set_mode((config.width, config.height))
        self.__font = pygame.font.Font(None, 30)
        self.__bg = None
        bg = spec.get("bg")
        if bg is not None:
            self.__bg = pygame.transform.smoothscale(pygame.image.load(bg).convert_alpha(), (config.width, config.bg_height))

    def run(self, inventory):
        if self.__spec["type"] == "ending":
            self.__show_ending()
            return TaskResult(success=True)
        self.__render_question()
        choice = self.__read_choice()
        result = evaluate(self.__spec, inventory, choice)
        inventory |= result.add_items
        inventory -= result.remove_items
        self.__render_feedback(result)
        return result

    def __read_choice(self):
        option_count = len(self.__spec["options"])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    number = event.key - pygame.K_1 + 1
                    if 1 <= number <= option_count:
                        return number

    def __render_question(self):
        if self.__bg is not None:
            self.__screen.blit(self.__bg, (0, 0))
        else:
            self.__screen.fill(config.bg_color)
        question = self.__spec.get("question")
        if question:
            self.__screen.blit(self.__font.render(question, True, config.text_color), (config.text_x, config.text_y - 15))
        for index, option in enumerate(self.__spec["options"]):
            x = config.text_x + (index % 2) * 350
            y = config.text_y + 25 + (index // 2) * 50
            self.__screen.blit(self.__font.render(option, True, config.text_color), (x, y))
        pygame.display.flip()

    def __render_feedback(self, result):
        if result.feedback:
            color = (0, 255, 0) if result.success else (255, 0, 0)
            self.__screen.blit(self.__font.render(result.feedback, True, color), (config.text_x, config.text_y + 50))
            pygame.display.flip()
            time.sleep(3)

    def __show_ending(self):
        self.__screen.fill(config.bg_color)
        font = pygame.font.Font(None, 45)
        message = self.__spec.get("message", "")
        self.__screen.blit(font.render(message, True, config.text_color), (150, 275))
        pygame.display.flip()
        time.sleep(5)