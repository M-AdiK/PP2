import pygame
import sys
import math

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

screen.fill(WHITE)

font = pygame.font.SysFont("Arial", 20)

drawing = False
last_pos = None
brush_size = 5
current_color = BLACK

eraser_mode = False
rectangle_mode = False
circle_mode = False

start_pos = None

palette = [
    (BLACK, pygame.Rect(10, 10, 40, 40)),
    (RED, pygame.Rect(60, 10, 40, 40)),
    (GREEN, pygame.Rect(110, 10, 40, 40)),
    (BLUE, pygame.Rect(160, 10, 40, 40)),
    (YELLOW, pygame.Rect(210, 10, 40, 40)),
]

eraser_button = pygame.Rect(270, 10, 100, 40)
rectangle_button = pygame.Rect(380, 10, 120, 40)
circle_button = pygame.Rect(510, 10, 100, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_ui = False

                for color, rect in palette:
                    if rect.collidepoint(event.pos):
                        current_color = color
                        eraser_mode = False
                        rectangle_mode = False
                        circle_mode = False
                        clicked_ui = True
                        break

                if eraser_button.collidepoint(event.pos):
                    eraser_mode = True
                    rectangle_mode = False
                    circle_mode = False
                    clicked_ui = True

                if rectangle_button.collidepoint(event.pos):
                    rectangle_mode = True
                    eraser_mode = False
                    circle_mode = False
                    clicked_ui = True

                if circle_button.collidepoint(event.pos):
                    circle_mode = True
                    rectangle_mode = False
                    eraser_mode = False
                    clicked_ui = True

                if not clicked_ui:
                    start_pos = event.pos

                    if rectangle_mode or circle_mode:
                        pass
                    else:
                        drawing = True
                        last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if rectangle_mode and start_pos is not None:
                    end_pos = event.pos

                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    rect_x = min(x1, x2)
                    rect_y = min(y1, y2)
                    rect_w = abs(x2 - x1)
                    rect_h = abs(y2 - y1)

                    pygame.draw.rect(screen, current_color, (rect_x, rect_y, rect_w, rect_h), 2)

                if circle_mode and start_pos is not None:
                    end_pos = event.pos

                    x1, y1 = start_pos
                    x2, y2 = end_pos

                    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

                    if radius > 0:
                        pygame.draw.circle(screen, current_color, (x1, y1), radius, 2)

                drawing = False
                last_pos = None
                start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos

                if eraser_mode:
                    draw_color = WHITE
                    draw_size = 20
                else:
                    draw_color = current_color
                    draw_size = brush_size

                pygame.draw.line(screen, draw_color, last_pos, current_pos, draw_size)
                last_pos = current_pos

    for color, rect in palette:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    pygame.draw.rect(screen, GRAY, eraser_button)
    pygame.draw.rect(screen, BLACK, eraser_button, 2)
    eraser_text = font.render("Eraser", True, BLACK)
    screen.blit(eraser_text, (eraser_button.x + 15, eraser_button.y + 10))

    pygame.draw.rect(screen, GRAY, rectangle_button)
    pygame.draw.rect(screen, BLACK, rectangle_button, 2)
    rectangle_text = font.render("Rectangle", True, BLACK)
    screen.blit(rectangle_text, (rectangle_button.x + 10, rectangle_button.y + 10))

    pygame.draw.rect(screen, GRAY, circle_button)
    pygame.draw.rect(screen, BLACK, circle_button, 2)
    circle_text = font.render("Circle", True, BLACK)
    screen.blit(circle_text, (circle_button.x + 18, circle_button.y + 10))

    pygame.display.update()