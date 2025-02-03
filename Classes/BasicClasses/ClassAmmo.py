import time

import pygame

from size import screen, WIDTH, HEIGHT

from functions.images_functions.loadimage import load_image



class Ammo(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.display, count_ammo, *groups):
        """
        Создаёт спрайт для декорации сцены
        :param image: Изображение декорации
        :param position: Позиция спрайта на экране
        :param flip: Флаг, указывающий, нужно ли отразить изображение горизонтально
        :param groups: Группы спрайтов, в которые будет добавлен спрайт
        """
        super().__init__(*groups)

        # Загружаем изображение прицела
        self.custom_cursor = load_image("images\PNG\HUD", "crosshair_white_large.png", -1)
        self.bullet = load_image("images\PNG\HUD", "icon_bullet_silver_short.png", -1)
        self.bullet_empty = load_image("images\PNG\HUD", "icon_bullet_empty_short.png", -1)

        self.screen = screen

        self.bullets_count = count_ammo
        self.bullets = [True] * self.bullets_count

        self.reload_time = 500  # Задержка восстановления одного патрона (в миллисекундах)
        self.reload_start_time = None
        self.current_reload_index = 0
        self.is_reloading = False

        self.bullet_positions = [(WIDTH - 30 - (i * 30), HEIGHT - 50) for i in range(self.bullets_count)]

    def update(self, *args):
        current_time = pygame.time.get_ticks()

        # Рисуем пули (с учетом их состояния)
        for i, bullet_position in enumerate(self.bullet_positions):
            # Если пуля пустая, рисуем пустую
            bullet_image = self.bullet_empty if not self.bullets[i] else self.bullet
            bullet_rect = bullet_image.get_rect(topleft=bullet_position)
            self.screen.blit(bullet_image, bullet_rect)

        if self.is_reloading and self.reload_start_time is not None:
            if current_time - self.reload_start_time >= self.reload_time:
                if self.current_reload_index < self.bullets_count:
                    self.bullets[self.current_reload_index] = True
                    print(f"Пуля {self.current_reload_index + 1} перезаряжена.")
                    self.current_reload_index += 1
                    self.reload_start_time = current_time
                else:
                    self.is_reloading = False
                    print("Перезарядка завершена!")

        # Обработка кликов на пули
        if (
            args 
            and args[0].type == pygame.MOUSEBUTTONDOWN 
        ):
            self.shoot()

        # Обработка нажатия клавиши R для перезарядки
        if (
            args 
            and args[0].type == pygame.KEYDOWN 
            and args[0].key == pygame.K_r
        ):
            self.reload()

    def shoot(self):
        """Метод для обработки выстрела"""
        if self.is_reloading:
            print("Идёт перезарядка! Стрельба невозможна.")
            return False
        
        if not any(self.bullets):  # Если все пули пустые
            pygame.mixer.Sound("sounds/осечка.mp3").play()
            print("Нет пуль! Нажмите R для перезарядки.")
            return False
    
        for i in range(self.bullets_count):
            if self.bullets[i]:  # Если пуля не пуста, то выстрел
                self.bullets[i] = False  # Сделать пулю пустой
                pygame.mixer.Sound("sounds/shoot.mp3").play()  # Звук выстрела
                print('Выстрел!')
                return True
            
        return False

    def reload(self):
        if all(self.bullets):
            print("Обойма полна, перезарядка невозможна.")
            return False

        """Инициализируем процесс перезарядки"""
        if not self.is_reloading:
            print("Начинаю перезарядку...")
            self.is_reloading = True
            self.current_reload_index = 0
            self.reload_start_time = pygame.time.get_ticks()