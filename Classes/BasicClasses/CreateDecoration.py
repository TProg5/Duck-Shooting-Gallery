import pygame
from functions.images_functions.loadimage import load_image

class Decoration(pygame.sprite.Sprite):
    def __init__(self, image, position, *groups, flip=False):
        """
        Создаёт спрайт для декорации сцены
        :image: Изображение декорации
        :position: Позиция спрайта на экране
        :flip: Флаг, указывающий, нужно ли отразить изображение горизонтально
        :groups: Группы спрайтов, в которые будет добавлен спрайт
        """
        super().__init__(*groups)

        if flip:
            image = pygame.transform.flip(image, True, False)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position
