import pygame
import random
from typing import Any

from Classes.BasicClasses.ClassDuck import Duck
from Classes.BasicClasses.CreateDecoration import Decoration
from Classes.BasicClasses.WaterClass import WaterRow
from Classes.BasicClasses.ClassCloud import Cloud
from functions.images_functions.loadimage import load_image


from size import screen, WIDTH, HEIGHT


class Background:
    def __init__(self, screen, wigth, height, duck_range: tuple, duck_speed: tuple):
        self.WIDTH, self.HEIGHT = wigth, height
        pygame.display.set_caption("Duck Shooting Gallery")
        
        self.screen = screen

        self.images = self.load_images()
        self.clock = pygame.time.Clock()

        # Sprite Groups
        self.curtain_sprite = pygame.sprite.Group()
        self.background_sprite = pygame.sprite.Group()
        self.main_ducks = pygame.sprite.Group()
        self.background_ducks = pygame.sprite.Group()
        self.cloud_sprite = pygame.sprite.Group()

        # Additional components
        self.top_water_row, self.bottom_water_row = self.create_water_rows()

        self.duck_speed = duck_speed
        self.count_duck_main, self.count_duck_background = duck_range[0], duck_range[1]
        self.speed_duck_main, self.speed_duck_background = duck_speed[0], duck_speed[1]

        self.running = True

        self.create_clouds()
        self.create_decorations()
        self.create_ducks()

    @staticmethod
    def initialize_pygame():
        pygame.init()

    @staticmethod
    def load_images() -> dict[str, Any]:
        stall_path = "images/PNG/Stall"
        objects_path = "images/PNG/Objects"
        hud_path = "images/PNG/HUD"
    
        return {
            "curtain_image": load_image(stall_path, "curtain.png", -1),
            "curtain_top_image": load_image(stall_path, "curtain_top.png", -1),
            "curtain_rope": load_image(stall_path, "curtain_rope.png", -1),
            "curtain_straight_image": load_image(stall_path, "curtain_straight.png", -1),
            "bg_red_image": load_image(stall_path, "bg_red.png"),
            "wood_scene": load_image(stall_path, "bg_wood.png"),
            "water1_image": load_image(stall_path, "water1.png", -1),
            "water2_image": load_image(stall_path, "water2.png", -1),
            "grass1_image": load_image(stall_path, "grass1.png"),
            "grass2_image": load_image(stall_path, "grass2.png"),
            "tree_oak_image": load_image(stall_path, "tree_oak.png"),
            "tree_pine_image": load_image(stall_path, "tree_pine.png"),
            "monotone_wood_texture": load_image(stall_path, "game_texture.png"),
            "rifle_image": load_image(objects_path, "rifle.png"),
            "cursor": load_image(hud_path, "crosshair_white_small.png")
        }

    def create_decorations(self):
        self.create_background()
        self.create_trees()
        self.create_grass()
        self.create_curtains()

    def create_background(self):
        for x in range(0, self.WIDTH, 250):
            Decoration(self.images["wood_scene"], (x, 0), self.background_sprite)

    def create_trees(self):
        Decoration(self.images["tree_oak_image"], (10, 15), self.background_sprite)
        Decoration(self.images["tree_pine_image"], (self.WIDTH - 130, 90), self.background_sprite)

    def create_grass(self):
        for x in range(0, self.WIDTH, 132):
            if random.random() < 0.3:
                Decoration(self.images["grass2_image"], (x, 214), self.background_sprite)
            else:
                Decoration(self.images["grass1_image"], (x, 230), self.background_sprite)

    def create_curtains(self):
        for x in range(0, self.WIDTH, 160):
            Decoration(self.images["curtain_top_image"], (x, 50), self.curtain_sprite)

        for x in range(0, self.WIDTH, 195):
            Decoration(self.images["monotone_wood_texture"], (x, self.HEIGHT - 100), self.curtain_sprite)

        Decoration(self.images["curtain_image"], (0, 0), self.curtain_sprite)
        Decoration(self.images["curtain_image"], (self.WIDTH - self.images["curtain_image"].get_width(), 0), self.curtain_sprite, flip=True)

        Decoration(self.images["curtain_rope"], (-5, 205), self.curtain_sprite)
        Decoration(self.images["curtain_rope"], (self.WIDTH - 35, 205), self.curtain_sprite, flip=True)

        bg_red_scaled = pygame.transform.scale(self.images["bg_red_image"], (self.WIDTH, self.HEIGHT // 8))
        Decoration(bg_red_scaled, (0, 0), self.curtain_sprite)

        for x in range(0, self.WIDTH, 256):
            Decoration(self.images["curtain_straight_image"], (x, 0), self.curtain_sprite)

    def create_ducks(self):
        for _ in range(1):
            x = random.randint(-300, 0)
            y = 160
            Duck(x, y, self.speed_duck_background, self.WIDTH, self.background_ducks)

        for _ in range(1):
            x = random.randint(-300, 0)
            y = 200
            Duck(x, y, self.speed_duck_main, self.WIDTH, self.main_ducks)

    def create_water_rows(self):
        scaled_water1 = self.images["water1_image"]
        scaled_water2 = self.images["water2_image"]

        top_water_row = WaterRow(290, scaled_water1, self.WIDTH, 5)
        bottom_water_row = WaterRow(310, scaled_water2, self.WIDTH, 70)

        return top_water_row, bottom_water_row

    def create_clouds(self):
        for _ in range(1):
            x = random.randint(-100, 0)
            y = 60
            Cloud(x, y, self.WIDTH, self.HEIGHT, self.cloud_sprite)

    def draw_layers(self, groups):
        for group in groups:
            group.draw(self.screen)

    def update(self):
        self.main_ducks.update()
        self.background_ducks.update()
        self.cloud_sprite.update()

        self.draw_layers([
            self.background_sprite,
            self.background_ducks,
            self.top_water_row,
            self.main_ducks,
            self.bottom_water_row,
            self.cloud_sprite,
            self.curtain_sprite,
        ])