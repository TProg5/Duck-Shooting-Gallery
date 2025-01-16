import pygame
import random
from functions.images_functions.loadimage import load_image


class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, wight, *groups):
        super().__init__(*groups)
        self.duck_types = [
            "duck_outline_target_brown.png",
            "duck_outline_target_white.png",
            "duck_outline_target_yellow.png"
        ]

        self.speed = speed
        self.wight = wight

        self.shot_down_duck = load_image("kenney_shooting-gallery\PNG\Objects", "duck_outline_back.png", -1)

        # Рандомно выбираем утку
        selected_duck = random.choice(self.duck_types)
        duck_image = load_image("kenney_shooting-gallery/PNG/Objects", selected_duck, -1)

        # Загружаем подставку
        stand_type = random.choice(["stick_woodFixed.png", "stick_metal.png"])
        stand_image = load_image("kenney_shooting-gallery/PNG/Objects", stand_type)

        # Создаём объединённое изображение
        self.image = pygame.Surface(
            (duck_image.get_width(), duck_image.get_height() + 100),  # Высота увеличена для подставки
            pygame.SRCALPHA  # Учитываем прозрачность
        )
        self.image.blit(stand_image, (40, 100))  # Рисуем подставку
        self.image.blit(duck_image, (0, 0))  # Рисуем утку сверху

        self.shot_image = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.shot_image.blit(stand_image, (40, 100))
        self.shot_image.blit(self.shot_down_duck, (0, 0))

                
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3

    def is_colliding(self, groups):
        """
        Проверяет, пересекается ли текущая утка с другими утками из всех переданных групп.
        """
        for group in groups:
            for duck in group:
                if duck != self and self.rect.colliderect(duck.rect): 
                    return True
        return False
    
    def update(self, *args):
        # Движение утки по экрану
        self.rect.x += self.speed

        # Возвращаем утку, если она вышла за пределы экрана
        if self.rect.right > self.wight + 100:
            self.rect.x = -self.rect.width

        if (
            args
            and args[0].type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(args[0].pos)
        ):
            self.image = self.shot_image  # Меняем текстуру
