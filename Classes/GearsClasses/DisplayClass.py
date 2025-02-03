import pygame
import time

from size import screen, WIDTH, HEIGHT


class Display:
    def __init__(self, screen):
        self.numbers = {f"{number}": pygame.image.load(f"images/PNG\HUD/text_{number}.png") for number in range(10)}
        self.small_numbers = {f"{number}": pygame.image.load(f"images/PNG\HUD/text_{number}_small.png") for number in range(10)}

        self.text_time_up = pygame.image.load("images/PNG/HUD/text_timeup.png")
        self.text_game_over = pygame.image.load("images/PNG/HUD/text_gameover.png")
        self.text_go = pygame.image.load("images/PNG/HUD/text_go.png")
        self.text_ready = pygame.image.load("images/PNG/HUD/text_ready.png")
        self.text_score_small = pygame.image.load("images/PNG/HUD/text_score_small.png")
        self.text_score = pygame.image.load("images\PNG\HUD/text_score.png")
        self.text_dot = pygame.image.load("images\PNG\HUD/text_dots.png")
        self.text_small_dot = pygame.image.load("images\PNG\HUD/text_dots_small.png")
        self.icon_duck = pygame.image.load("images\PNG\HUD/icon_duck.png")

        self.screen = screen

        screen_width, screen_height = self.screen.get_size()
        # Центр координат для размещения текста
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2

        # Затемняющий слой
        self.overlay_color = (0, 0, 0)
        self.overlay_alpha = 150
        self.overlay_surface = pygame.Surface((WIDTH, HEIGHT))
        self.overlay_surface.set_alpha(self.overlay_alpha)
        self.overlay_surface.fill(self.overlay_color)

    def blit_start_level(self):
        # Время между отображением чисел
        countdown_time = 0.9  # в секундах

        # Обратный отсчёт: 3, 2, 1
        for num in ["3", "2", "1"]:
            self.screen.fill((0, 0, 0))  # Очистка экрана
            number_image = self.numbers[num]
            number_rect = number_image.get_rect(center=(self.center_x, self.center_y))
            self.screen.blit(number_image, number_rect)
            pygame.display.flip()
            time.sleep(countdown_time)

        # "Ready?" отображение
        self.screen.fill((0, 0, 0))  # Очистка экрана
        ready_rect = self.text_ready.get_rect(center=(self.center_x, self.center_y))
        self.screen.blit(self.text_ready, ready_rect)
        pygame.display.flip()
        time.sleep(countdown_time)

        # "Go!" отображение
        self.screen.fill((0, 0, 0))  # Очистка экрана
        go_rect = self.text_go.get_rect(center=(self.center_x, self.center_y))
        self.screen.blit(self.text_go, go_rect)
        pygame.display.flip()
        time.sleep(countdown_time)
    
    def time_up(self):
        """Отображение надписи Time Up с блокировкой карты."""
        self.screen.blit(self.overlay_surface, (0, 0))  # Затемнить фон
        time_up_rect = self.text_time_up.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.screen.blit(self.text_time_up, time_up_rect)  # Отобразить текст
        pygame.display.flip()

    def game_over(self):
        """Отображение надписи Game Over с блокировкой карты."""
        self.screen.blit(self.overlay_surface, (0, 0))  # Затемнить фон
        game_over_rect = self.text_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(self.text_game_over, game_over_rect)  # Отобразить текст
        pygame.display.flip()

    def blit_score(self, score, position: tuple):
        """
        Отображение текущего счета игры в формате "Score: X".
        """
        # Вывод текста "Score"
        text_score_rect = self.text_score.get_rect(midleft=(position[0], position[1]))
        self.screen.blit(self.text_score_small, text_score_rect.topleft)

        # Вывод двоеточия (опционально, если нужно визуально отделить текст)
        text_small_dot_rect = self.text_dot.get_rect(midleft=(text_score_rect.right - 75, position[1] - 10))
        self.screen.blit(self.text_small_dot, text_small_dot_rect.topleft)

        # Вывод числового значения счета
        x_offset = text_small_dot_rect.right + 2
        for digit in str(score):
            if digit in self.numbers:
                number_image = self.small_numbers[digit]
                number_rect = number_image.get_rect(midleft=(x_offset, position[1] - 10))
                self.screen.blit(number_image, number_rect.topleft)
                x_offset += number_image.get_width() + 1  # Отступ между цифрами

    def blit_time(self, time_remaining, position: tuple):
        """
        Отображение оставшегося времени по разрядам.
        """
        digits = list(str(time_remaining))
        x_offset = position[0]
        for digit in digits:
            if digit in self.numbers:
                number_image = self.small_numbers[digit]
                self.screen.blit(number_image, (x_offset, position[1]))
                x_offset += number_image.get_width() + 1  # Добавляем расстояние между цифрами

    def blit_ducks(self, ducks, position: tuple):
        screen.blit(self.icon_duck, position)

        digits = list(str(int(ducks)))  
        x_offset = position[0]
        for digit in digits:
            if digit in self.numbers:
                number_image = self.small_numbers[digit]
                self.screen.blit(number_image, (x_offset + 40, position[1]))
                x_offset += number_image.get_width() + 3  # Добавляем расстояние между цифрами


class ResultDisplay:
    def __init__(self, screen):
        self.screen = screen

        # Затемняющий слой
        self.overlay_color = (0, 0, 0)
        self.overlay_alpha = 150
        self.overlay_surface = pygame.Surface(self.screen.get_size())
        self.overlay_surface.set_alpha(self.overlay_alpha)
        self.overlay_surface.fill(self.overlay_color)

        self.font = pygame.font.Font(None, 48)  # Или укажите путь к файлу шрифта
        self.text_color = (255, 255, 255)


    def draw_results(self, time, ducks_shot):
        """Вывод результатов на затемнённый экран."""
        self.screen.blit(self.overlay_surface, (0, 0))  # Затемнить экран

        # Текст: количество сбитых уток
        ducks_text = f"Ducks shot: {ducks_shot}"
        ducks_surface = self.font.render(ducks_text, True, self.text_color)
        ducks_rect = ducks_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(ducks_surface, ducks_rect)

        # Текст: время прохождения уровня
        time_text = f"Time: {time} seconds"
        time_surface = self.font.render(time_text, True, self.text_color)
        time_rect = time_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        self.screen.blit(time_surface, time_rect)

        pygame.display.flip()  # Обновить экран