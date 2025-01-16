import pygame


class Level:
    def __init__(self, screen, difficulty, duration, duck_count, duck_speed):
        self.screen = screen

        self.numbers = {f"{number}": pygame.image.load(f"kenney_shooting-gallery\PNG\HUD/text_{number}.png") for number in range(10)}

        self.difficulty = difficulty
        self.time_left = duration
        self.total_ducks = duck_count
        self.duck_speed = duck_speed
        self.remaining_ducks = duck_count
        self.shot_ducks = 0
        self.font = pygame.font.Font(None, 36)
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)  # Таймер уменьшает время каждую секунду

    def update(self):
        # Отображаем счетчик и таймер
        self.display_status()

    def display_status(self):
        timer_text = self.font.render(f"Time: {self.time_left}s", True, (255, 0, 0))
        score_text = self.font.render(f"Score: {self.shot_ducks}", True, (255, 255, 255))
        ducks_text = self.font.render(f"Ducks Left: {self.remaining_ducks}", True, (0, 255, 0))

        self.screen.blit(timer_text, (800, 10))
        self.screen.blit(score_text, (800, 50))
        self.screen.blit(ducks_text, (800, 90))

    def handle_event(self, event):
        if event.type == self.timer_event:
            self.time_left -= 1

        if self.time_left <= 0 or self.remaining_ducks <= 0:
            self.end_level()

    def duck_shot(self):
        self.shot_ducks += 1
        self.remaining_ducks -= 1

    def end_level(self):
        # Конец уровня или переход к следующему
        print(f"Level {self.difficulty} complete! Total score: {self.shot_ducks}")
        pygame.time.set_timer(self.timer_event, 0)  # Останавливаем таймер
