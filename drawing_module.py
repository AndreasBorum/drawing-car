import pygame

class Drawing_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface((200,200))
        self.rect = self.surface.get_rect()
        self.surface.fill('blue')
        pygame.draw.circle(self.surface,'red',(100,100),50,3)

        self.is_drawing= False
        self.dots=[]

    def drawing(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.math.Vector2.distance_to(pygame.Vector2(self.dots[-1]), pygame.Vector2(pos)) > 40:
            self.dots.append(pos)

    def draw(self, parrent_surface):
        if self.is_drawing:
            self.drawing()
        if len(self.dots)>1:
            pygame.draw.lines(self.surface, 'black', False, self.dots)
        parrent_surface.blit(self.surface,(100,300))

    def surface_clicked(self):
        if not self.is_drawing:
            self.dots.clear()
            self.dots.append(pygame.mouse.get_pos())
        self.is_drawing = True