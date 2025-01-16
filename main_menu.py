import pygame
import random
from functions.browser_functions.browser_open import open_link
from Classes.GearsClasses.DisplayClass import Display
from Classes.GearsClasses.ClassBackground import Background
from Classes.BasicClasses.ClassButton import Button

from game import CreateGame

SIZE = WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode(SIZE)

def start_game(screen):
    game = CreateGame((random.randint(1, 4), random.randint(1, 5)), (3, 4))
    display = Display(screen)

    display.blit_start_level()
    game.run()


class Buttons(pygame.sprite.Group):
    def __init__(self, screen, controller):
        super().__init__()
        self.screen = screen
        self.controller = controller
        self.button_play = Button("button_play.png", (50, 120))
        self.button_endless_mode = Button("button_endless_mode.png", (50, 220))
        self.button_about_the_author = Button("button_about_the_author.png", (50, 320))
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
        self.ButtonEasy = Button("ButtonEasy.png", (370, 120))
        self.ButtonMedium = Button("ButtonMedium.png", (370, 220))
        self.ButtonHard = Button("ButtonHard.png", (370, 320))
        self.add(self.ButtonEasy, self.ButtonMedium, self.ButtonHard)

        self.display = Display(self.screen)

    def handler_clicks(self):
        for button in self:
            if button.clicked:
                if button is self.ButtonEasy:
                    print("ButtonEasy clicked!")
                    start_game(screen)

                elif button is self.ButtonMedium:
                    print("ButtonMedium clicked!")
                    start_game(screen)

                elif button is self.ButtonHard:
                    print("ButtonHard clicked!")
                    start_game(screen)


class MenuController:
    def __init__(self, screen):
        self.screen = screen
        self.state = "main_menu"  # Текущее состояние меню
        self.buttons = Buttons(screen, self)
        self.buttons_levels = ButtonLevels(screen, self)
        self.background = Background(screen, WIDTH, HEIGHT, (random.randint(1, 4), random.randint(1, 5)), (3, 4))

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
    screen = pygame.display.set_mode((1000, 500))
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
