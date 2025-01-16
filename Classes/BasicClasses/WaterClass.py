class WaterRow:
    def __init__(self, y, water_image, screen_width, deviation=0):
        self.y = y
        self.water_image = water_image
        self.water_width = water_image.get_width()
        self.water_row = []

        # Вычисляем, сколько плиток воды нужно, чтобы заполнить ширину экрана
        for x in range(0, screen_width, self.water_width):
            self.water_row.append((water_image, (x - deviation, y)))

    def draw(self, screen):
        for water, position in self.water_row:
            screen.blit(water, position)
