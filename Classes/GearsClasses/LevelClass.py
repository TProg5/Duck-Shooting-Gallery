import json
import pygame

from Classes.GearsClasses.DisplayClass import Display, ResultDisplay
from functions.data_functions.json_functions import check_progress_level, data_json, lvl_points
from functions.data_functions.json_functions import update_admit, update_progress

SIZE = WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode(SIZE)


class LevelControl:
    def __init__(self, screen, duration, difficulty, next_difficulty, duck_count, duck_speed, return_to_menu):
        self.screen = screen

        self.numbers = {
            f"{number}": pygame.image.load(
                f"images\PNG\HUD/text_{number}.png"
            )
            for number in range(10)
        }

        self.return_to_menu = return_to_menu

        self.time = duration
        self.duck_count = duck_count
        self.points = 0
        self.one_duck_points = lvl_points(f"Levels", f"{difficulty}.json")
        self.difficulty = difficulty
        self.next_difficulty = next_difficulty
        self.time_left = duration
        self.total_ducks = duck_count
        self.duck_speed = duck_speed
        self.remaining_ducks = duck_count
        self.shot_ducks = 0
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(
            self.timer_event, 1000
        )  # Таймер уменьшает время каждую секунду

        self.display = Display(screen)
        self.result_display = ResultDisplay(screen)

    def update(self):
        # Отображаем счетчик и таймер
        self.display_status()

    def display_status(self):
        self.display.blit_time(self.time_left, (920, 15))
        self.display.blit_score(self.points, (30, 460))
        self.display.blit_ducks(self.remaining_ducks, (10, 10))

    def handle_event(self, event):
        if event.type == self.timer_event:
            self.time_left -= 1

        if self.time_left <= 0 and self.remaining_ducks > 0:

            self.display.time_up()  # Вывод надписи Time Up
            self.block_for_duration(2000)  # Блокируем карту на 2 секунды
            
            self.display.game_over()  # Вывод надписи Game Over
            self.block_for_duration(2000)  # Блокируем карту на 2 секунды
            
            self.end_level()  # Конец уровня и вывод результатов

        if self.time_left > 0 and self.remaining_ducks <= 0:
            print(f"Level {self.difficulty} complete! Total score: {self.shot_ducks}")
            update_admit("Levels", f"{self.next_difficulty}.json")
            update_progress("Levels", f"{self.difficulty}.json")

            self.end_level()


    def duck_shot(self):
        self.shot_ducks += 1
        self.remaining_ducks -= 1
        self.points += self.one_duck_points

    def end_level(self):
        pygame.time.set_timer(self.timer_event, 0)  # Останавливаем таймер

        self.result_display.draw_results(self.time - self.time_left, self.shot_ducks)
        self.block_for_duration(5000)

        self.return_to_menu()
        
    def block_for_duration(self, milliseconds):
        """Блокирует карту, не обрабатывает события в течение указанного времени."""
        block_start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - block_start < milliseconds:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Позволяет выйти из игры
                    return
