import pygame

SURFACE_SIZE = (200,200)
SURFACE_POS = (400,300)

class Car_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect=self.rect.move(SURFACE_POS)


    def draw(self, parrent_surface):
        self.surface.fill('blue')

        parrent_surface.blit(self.surface,SURFACE_POS)
