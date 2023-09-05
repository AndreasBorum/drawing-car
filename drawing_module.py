import pygame

SURFACE_SIZE = (200,200)
SURFACE_POS = (100,300)

class Drawing_surface():
    def __init__(self) -> None:
        self.surface = pygame.Surface(SURFACE_SIZE)
        self.rect = self.surface.get_rect()
        self.collide_rect=self.rect.move(SURFACE_POS)


        self.is_drawing= False
        self.dots=[]

    def drawing(self):
        pos = tuple(map(lambda i, j: i - j, pygame.mouse.get_pos(), SURFACE_POS))
        if len(self.dots)==0:
            self.dots.append(pos)
        elif self.rect.collidepoint(pos) and pygame.math.Vector2.distance_to(pygame.Vector2(self.dots[-1]), pygame.Vector2(pos)) > 40:
            self.dots.append(pos)

    def draw(self, parrent_surface):
        self.surface.fill('blue')
        if self.is_drawing:
            self.drawing()
        if len(self.dots)>1:
            pygame.draw.lines(self.surface, 'black', False, self.dots, 5)
        parrent_surface.blit(self.surface,SURFACE_POS)

    def surface_clicked(self):
        print('clicked')
        if not self.is_drawing:
            self.dots.clear()
        self.is_drawing = True
    
    def surface_unclicked(self):
        print('unclicked')
        if self.is_drawing:
            self.is_drawing = False