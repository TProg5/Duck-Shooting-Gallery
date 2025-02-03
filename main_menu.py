import pygame
import random

from size import screen, WIDTH, HEIGHT

from functions.browser_functions.browser_open import open_link
from Classes.GearsClasses.DisplayClass import Display
from Classes.GearsClasses.ClassBackground import Background
from Classes.BasicClasses.ClassButton import Button

from CreateGameClass import CreateGame

from functions.data_functions.json_functions import data_json, check_progress_level, check_admit


def return_to_menu():
    pygame.mouse.set_visible(True)
    print("Returning to main menu...")
    menu()

def start_game(screen, count_duck: tuple, duck_speed: tuple, difficulty, next_difficulty):
    game = CreateGame(count_duck, duck_speed, difficulty, next_difficulty, return_to_menu = return_to_menu)
    display = Display(screen)

    display.blit_start_level()
    game.run()
    
    
class Buttons(pygame.sprite.Group):
    def __init__(self, screen, controller):
        super().__init__()
        self.screen = screen
        self.controller = controller
        self.button_play = Button("images/PNG/Buttons/button_play.png", (50, 120))
        self.button_endless_mode = Button("images/PNG/Buttons/button_endless_mode.png", (50, 220))
        self.button_about_the_author = Button("images/PNG/Buttons/button_about_the_author.png", (50, 320))
        self.add(self.button_play, self.button_endless_mode, self.button_about_the_author)

    def handler_clicks(self):
        for button in self:
            if button.clicked:
                if button is self.button_play:
                    print("Play button clicked!")
                    self.controller.set_state("level_menu")

                elif button is self.button_endless_mode:
                    pass

                elif button is self.button_about_the_author:
                    print("About the author button clicked!")
                    open_link("https://github.com/TProg5")


class ButtonLevels(pygame.sprite.Group):
    def __init__(self, screen, controller):
        super().__init__()
        self.screen = screen
        self.controller = controller

        # Порядок уровней
        self.difficulties = ["easy", "medium", "hard"]
        
        # Инициализация кнопок с учётом прогресса
        self.ButtonEasy = self.create_button(0, "ButtonEasy.png", None, (370, 120))
        self.ButtonMedium = self.create_button(1, "ButtonMedium.png", "ButtonMediumLock.png", (370, 220))
        self.ButtonHard = self.create_button(2, "ButtonHard.png", "ButtonHardLock.png", (370, 320))

        self.add(self.ButtonEasy, self.ButtonMedium, self.ButtonHard)
        self.display = Display(self.screen)

    def create_button(self, index, texture, locked_texture: None, position):
        """
        Создаёт кнопку, меняя её текстуру в зависимости от прогресса уровня.
        """

        if index == 0:
            return Button(f"images/PNG/Buttons/{texture}", position)
        
        else:
            if check_progress_level("Levels", f"{self.difficulties[index - 1]}.json"):
                return Button(f"images/PNG/Buttons/{texture}", position)
            
            else:
                return Button(f"images/PNG/Buttons/{locked_texture}", position)

    def handler_clicks(self):
        for button in self:
            if button.clicked:
                self.handle_button_click(button)

    def handle_button_click(self, button):
        """
        Обрабатывает нажатие кнопки, запуская соответствующий уровень.
        """
        difficulties = {
            self.ButtonEasy: "easy",
            self.ButtonMedium: "medium",
            self.ButtonHard: "hard"
        }

        difficulty = difficulties.get(button)
        
        if difficulty and check_admit("Levels", f"{difficulties[button]}.json"):
            print(f"{difficulty.capitalize()} Button clicked!")
            data = data_json("Levels", f"{difficulty}.json")

            # Определяем индекс текущего уровня
            index = self.difficulties.index(difficulty)
            next_difficulty = self.difficulties[index + 1] if index + 1 < len(self.difficulties) else None

            start_game(self.screen, 
                       (data["count_ducks"] / 2, data["count_ducks"] / 2), 
                       (data["ducks_speed"] + 1, data["ducks_speed"]),
                       difficulties[button],
                       next_difficulty)


class MenuController:
    def __init__(self, screen):
        self.screen = screen
        self.state = "main_menu"  # Текущее состояние меню
        self.buttons = Buttons(screen, self)
        self.buttons_levels = ButtonLevels(screen, self)
        self.background = Background(screen, WIDTH, HEIGHT, (random.randint(1, 4), random.randint(1, 5)), (2, 2))

    def set_state(self, state):
        """Устанавливает текущее состояние меню."""
        self.state = state

    def update(self, event):
        """Обновляет активные элементы интерфейса в зависимости от состояния."""
        if self.state == "main_menu":
            self.buttons.update(event)
            self.buttons.handler_clicks()

        elif self.state == "level_menu":
            self.buttons_levels.update(event)
            self.buttons_levels.handler_clicks()

    def draw(self):
        """Отрисовывает активные элементы интерфейса."""
        self.background.update()
        if self.state == "main_menu":
            self.buttons.draw(self.screen)

        elif self.state == "level_menu":
            self.buttons_levels.draw(self.screen)


def menu():
    pygame.init()
    pygame.display.set_caption("Duck Shooting Gallery")
    clock = pygame.time.Clock()

    controller = MenuController(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            controller.update(event)

        # Отрисовка
        screen.fill((255, 255, 255))
        controller.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    menu()
