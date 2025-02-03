import pygame
import random
from functions.images_functions.loadimage import load_image


class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *groups):
        """
        Создаёт спрайт для облака.
        :param x: Начальная позиция X.
        :param y: Начальная позиция Y.
        :param width: Ширина экрана.
        :param height: Высота экрана.
        :param groups: Группы, в которые добавляется спрайт.
        """
        super().__init__(*groups)

        # Загружаем случайное изображение облака
        cloud_types = ["cloud1.png", "cloud2.png"]  # Замените на реальные имена файлов

        selected_cloud = random.choice(cloud_types)
        self.image = load_image(
            "images\PNG\Stall", selected_cloud, -1
        )

        scale_factor = random.uniform(
            0.8, 1.2
        )  # Размер облака от 80% до 120% оригинала
        self.image = pygame.transform.scale(
            self.image,
            (
                int(self.image.get_width() * scale_factor),
                int(self.image.get_height() * scale_factor),
            ),
        )

        self.rect = self.image.get_rect(topleft=(x, y))
        self.width = width
        self.speed = random.choice([0.5, 0.75])  # Скорость перемещения облака

    def update(self, *args):
        """
        Обновляет позицию облака.
        """
        self.rect.x += self.speed

        # Если облако вышло за экран, возвращаем его назад
        if self.rect.left > self.width + 100:
            self.rect.right = 0
            self.rect.y = 60
