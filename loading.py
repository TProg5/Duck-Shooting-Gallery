import pygame
import sys

# Инициализация PyGame
pygame.init()

# Размеры окна и цвета
WIDTH, HEIGHT = 1000, 500
BG_COLOR = (0, 0, 0)  # Черный фон
TEXT_COLOR = (255, 255, 255)  # Белый текст

# Шрифты и текст
pygame.font.init()
font_small = pygame.font.SysFont('Arial', 24)
font_large = pygame.font.SysFont('Arial', 48)

# Создаем окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Shooting Gallery")

# Отрисовка текста и логотипа
def draw_splash():
    screen.fill(BG_COLOR)

    # Текст "Made with"
    text_made_with = font_small.render("Made with", True, TEXT_COLOR)
    made_with_rect = text_made_with.get_rect(center=(WIDTH // 3, HEIGHT // 3))
    screen.blit(text_made_with, made_with_rect)

    # Логотип PyGame (подставьте правильный путь к файлу)
    logo = pygame.image.load("pygame_logo.png")
    logo_rect = logo.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(logo, logo_rect)


# Основной игровой цикл
clock = pygame.time.Clock()
running = True

def splash_screen():
    timer = 0  # Для ограничения времени заставки (например, 3 секунды)
    while timer < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_splash()
        pygame.display.flip()
        clock.tick(60)
        timer += 1 / 60  # Добавляем время между кадрами

    # После заставки переходим к игре или меню
    print("Заставка завершена")
