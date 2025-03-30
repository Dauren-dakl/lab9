import pygame 
import os

pygame.init()
os.chdir(r"C:\\Users\\Acer\\Desktop\\PP2")

screen = pygame.display.set_mode((1080, 900))
clock = pygame.time.Clock()

# Определение цветов
RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

eraser = pygame.image.load('erase.jpg')
eraser = pygame.transform.scale(eraser, (70, 70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (index*40, 0, 40, 40))

def draw_circle(surface, color, pos, radius=40):
    pygame.draw.circle(surface, color, pos, radius)

def draw_rectangle(surface, color, pos):
    x, y = pos
    pygame.draw.rect(surface, color, (x - 35, y - 20, 70, 40))

def draw_square(surface, color, pos, size=50):
    x, y = pos
    pygame.draw.rect(surface, color, (x - size//2, y - size//2, size, size))

def draw_right_triangle(surface, color, pos, size=50):
    x, y = pos
    points = [(x, y), (x, y - size), (x + size, y)]
    pygame.draw.polygon(surface, color, points)

def draw_equilateral_triangle(surface, color, pos, size=50):
    x, y = pos
    height = (size * (3 ** 0.5)) / 2
    points = [(x, y - height//2), (x - size//2, y + height//2), (x + size//2, y + height//2)]
    pygame.draw.polygon(surface, color, points)

def draw_rhombus(surface, color, pos, size=50):
    x, y = pos
    points = [(x, y - size), (x - size, y), (x, y + size), (x + size, y)]
    pygame.draw.polygon(surface, color, points)

def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0 <= x <= 40 and 0 <= y <= 40:
            return RED
        elif 40 < x <= 80 and 0 <= y <= 40:
            return GREEN
        elif 80 < x <= 120 and 0 <= y <= 40:
            return BLUE
        elif 1010 <= x <= 1080 and 0 <= y <= 40:
            return BLACK
        elif 180 <= x <= 220 and 0 <= y <= 40:
            return "circle"
        elif 230 <= x <= 270 and 0 <= y <= 40:
            return "rectangle"
        elif 280 <= x <= 320 and 0 <= y <= 40:
            return "square"
        elif 330 <= x <= 370 and 0 <= y <= 40:
            return "right_triangle"
        elif 380 <= x <= 420 and 0 <= y <= 40:
            return "equilateral_triangle"
        elif 430 <= x <= 470 and 0 <= y <= 40:
            return "rhombus"
    return color

def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color == 'circle':
            draw_circle(screen, WHITE, (x, y))
        elif color == 'rectangle':
            draw_rectangle(screen, WHITE, (x, y))
        elif color == 'square':
            draw_square(screen, WHITE, (x, y))
        elif color == 'right_triangle':
            draw_right_triangle(screen, WHITE, (x, y))
        elif color == 'equilateral_triangle':
            draw_equilateral_triangle(screen, WHITE, (x, y))
        elif color == 'rhombus':
            draw_rhombus(screen, WHITE, (x, y))
        else:
            pygame.draw.circle(screen, color, (x, y), 27)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for i in range(len(colors)):
        draw_rect(i)
    
    screen.blit(eraser, (1010, 0))
    pygame.draw.circle(screen, WHITE, (200, 20), 20)
    pygame.draw.rect(screen, WHITE, (230, 10, 40, 40))
    pygame.draw.rect(screen, WHITE, (280, 10, 40, 40))  # Square
    pygame.draw.polygon(screen, WHITE, [(330, 50), (330, 10), (370, 50)])  # Right triangle
    pygame.draw.polygon(screen, WHITE, [(380, 30), (360, 50), (400, 50)])  # Equilateral triangle
    pygame.draw.polygon(screen, WHITE, [(430, 30), (450, 10), (470, 30), (450, 50)])  # Rhombus
    
    color = pick_color()
    painting(color)

    clock.tick(60)
    pygame.display.update()