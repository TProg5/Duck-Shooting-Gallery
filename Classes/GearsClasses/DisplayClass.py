import pygame
import time

SIZE = WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode(SIZE)


class Display:
    def __init__(self, screen):
        self.numbers = {f"{number}": pygame.image.load(f"kenney_shooting-gallery\PNG\HUD/text_{number}.png") for number in range(10)}
        self.text_go = pygame.image.load("kenney_shooting-gallery\PNG\HUD/text_go.png")
        self.text_ready = pygame.image.load("kenney_shooting-gallery\PNG\HUD/text_ready.png")
        self.text_score_small = pygame.image.load("kenney_shooting-gallery\PNG\HUD/text_score_small.png")

        self.screen = screen

        screen_width, screen_height = self.screen.get_size()
        # Центр координат для размещения текста
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2

    def blit_start_level(self):
        # Время между отображением чисел
        countdown_time = 1  # в секундах

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
    
    def game_over(self):
        game_over_rect = self.game_over.get_rect(center=(self.center_x, self.center_y))
        self.screen.blit(self.game_over, game_over_rect)

'''pygame.init()
screen = pygame.display.set_mode((1000, 500))
display = Display(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.blit_start_level()
    # Переместить ниже после отображения уровня:
    running = False

pygame.quit()'''
