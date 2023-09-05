import pygame


class Button():
    def __init__(self, size, pos) -> None:
        self.pos =pos
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.collide_rect=self.rect.move(pos)


    def draw(self, parrent_surface):
        if self.collide_rect.collidepoint(pygame.mouse.get_pos()):
            self.surface.fill('blue')
        else: 
            self.surface.fill('red')
        parrent_surface.blit(self.surface,self.pos)
    
    def on_press(self, function):
        function()

