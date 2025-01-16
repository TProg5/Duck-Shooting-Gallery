import pygame
from functions.images_functions.loadimage import load_image

WIDTH, HEIGHT = 1000, 500


class Rifle(pygame.sprite.Sprite):
    def __init__(self, screen, image, position, *groups, flip=False):
        """
        Ружье (анимация и отображение).
        :param screen: Экран для отрисовки.
        :param image: Изображение ружья.
        :param position: Позиция ружья.
        :param flip: Флаг, указывающий на отражение изображения.
        :param groups: Группы спрайтов.
        """
        super().__init__(*groups)

        if flip:
            image = pygame.transform.flip(image, True, False)

        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.screen = screen

        # Переменные для анимации отдачи
        self.is_recoiling = False  # Флаг анимации отдачи
        self.recoil_step = 0       # Текущее смещение при отдаче
        self.recoil_speed = 3      # Скорость смещения
        self.recoil_limit = 15     # Максимальное смещение назад

        # Переменная для обработки нажатий мыши
        self.shoot_event = False

    def update(self, event=None):
        pass
        ''' """
        Обрабатывает события и выполняет анимацию ружья.
        :param event: Событие pygame, необязательно.
        """

        self.is_recoiling = True
        self.recoil_step = 0
        self.shoot_event = True

        # Если анимация отдачи активна, выполняем смещение
        if self.is_recoiling:
            self.recoil_step += self.recoil_speed
            self.rect.y += self.recoil_speed  # Смещение назад (вниз)

            if self.recoil_step >= self.recoil_limit:  # Конец анимации
                self.is_recoiling = False
                self.rect.y -= self.recoil_step  # Возвращаем ружье в исходное положение
                self.shoot_event = False  # Сбрасываем событие выстрела

        # Отрисовка
        self.screen.blit(self.image, self.rect)'''