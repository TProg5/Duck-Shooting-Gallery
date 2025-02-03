import pygame

from main_menu import MenuController

pygame.init()

SIZE = WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode(SIZE)

class GameStateManager:
    def __init__(self):
        self.state = "MENU"
        self.clock = pygame.time.Clock()

    def set_state(self, state):
        """Устанавливает текущее состояние меню."""
        self.state = state    
        
    def update(self, event):
        if self.state == "MENU":
            pygame.display.set_caption("Duck Shooting Gallery")
            
            controller = MenuController(screen)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    controller.update(event)

                # Отрисовка
                screen.fill((255, 255, 255))
                controller.draw()
                pygame.display.flip()
                self.clock.tick(60)

            pygame.quit()

        elif self.state == "GAME":
            self.state = self.run_game()

        elif self.state == "RESULTS":
            self.state = self.show_results()

if __name__ == "__main__":
    
    clock = pygame.time.Clock()

    gamestate = GameStateManager()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            gamestate.update(event)

        # Отрисовка
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()