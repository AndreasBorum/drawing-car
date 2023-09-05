import pygame
import sys

from drawing_module import Drawing_surface

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#----------------------------------------------

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Coordinates Relative to Rectangle")

# Define two rectangles
drawing_rect_pos = (100, 100)
drawing_rect = pygame.Rect(*drawing_rect_pos, 200, 200)
car_rect_pos = (400,100)
car_rect = pygame.Rect(*car_rect_pos, 200, 200)

# Colors for the rectangles
drawing_rect_color = WHITE
car_rect_color = WHITE

def mouse_relative_pos(mouse_pos,rect):
    return mouse_pos[0] - rect.left, mouse_pos[1] - rect.top

car_vectors =[]
for point in [(0,0),(20,0),(10,20)]:
    car_vectors.append(pygame.math.Vector2(point))
car_pos = car_rect_pos
car_vectors = [vector.rotate(10) for vector in car_vectors]
print(car_vectors)

is_drawing= False
dots=[]
def drawing():
    pos = pygame.mouse.get_pos()
    if drawing_rect.collidepoint(pos) and pygame.math.Vector2.distance_to(pygame.Vector2(dots[-1]), pygame.Vector2(pos)) > 40:
        dots.append(pos)

drawing_surface = Drawing_surface()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if drawing_rect.collidepoint(event.pos):
                if not is_drawing:
                    dots.clear()
                    dots.append(event.pos)
                is_drawing = True
                if drawing_surface.rect.collidepoint(event.pos):
                    drawing_surface.surface_clicked()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("up")
            if is_drawing:
                is_drawing = False
        

    # Clear the screen
    screen.fill(BLACK)

    # Draw the rectangles
    pygame.draw.rect(screen, drawing_rect_color, drawing_rect)
    pygame.draw.rect(screen, car_rect_color, car_rect)

    pygame.draw.polygon(screen,RED,[point+car_pos for point in car_vectors ])


    if is_drawing:
        drawing()

    if len(dots)>1:
        pygame.draw.lines(screen, BLACK, False, dots)

    # Get the mouse coordinates relative to drawing_rect
    mouse_pos=pygame.mouse.get_pos()
    relative_x, relative_y = mouse_relative_pos(mouse_pos, drawing_rect)

    # Check if the mouse is inside drawing_rect
    if drawing_rect.collidepoint(mouse_pos):
        text = f"Mouse coordinates relative to drawing_rect: ({relative_x}, {relative_y})"
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (10, 10))

    drawing_surface.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
