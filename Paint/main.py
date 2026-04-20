import pygame
import sys
import math
from datetime import datetime

pygame.init()

WIDTH = 1000
HEIGHT = 700
CANVAS_Y = 80  # Top toolbar height

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

font = pygame.font.SysFont("Arial", 18)
small_font = pygame.font.SysFont("Arial", 14)

# Tool states
current_color = BLACK
brush_sizes = [2, 5, 10]
brush_index = 1
eraser_mode = False

# Shape modes
rectangle_mode = False
circle_mode = False
square_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False

# New tools
pencil_mode = True      # Default
line_mode = False
fill_mode = False
text_mode = False

text_input = ""
text_pos = None

start_pos = None
last_pos = None
drawing = False

# Palette
palette = [
    (BLACK, pygame.Rect(10, 10, 40, 40)),
    (RED, pygame.Rect(60, 10, 40, 40)),
    (GREEN, pygame.Rect(110, 10, 40, 40)),
    (BLUE, pygame.Rect(160, 10, 40, 40)),
    (YELLOW, pygame.Rect(210, 10, 40, 40)),
]

# Buttons
eraser_button = pygame.Rect(270, 10, 80, 40)
line_button = pygame.Rect(360, 10, 70, 40)
fill_button = pygame.Rect(440, 10, 60, 40)
text_button = pygame.Rect(510, 10, 70, 40)

size_buttons = [
    pygame.Rect(590, 10, 40, 40),  # Small
    pygame.Rect(640, 10, 40, 40),  # Medium
    pygame.Rect(690, 10, 40, 40)   # Large
]

# Old shape buttons
rectangle_button = pygame.Rect(750, 10, 90, 40)
circle_button = pygame.Rect(850, 10, 70, 40)
square_button = pygame.Rect(930, 10, 60, 40)

right_tri_button = pygame.Rect(10, 60, 110, 35)
eq_tri_button = pygame.Rect(130, 60, 120, 35)
rhombus_button = pygame.Rect(260, 60, 90, 35)

def flood_fill(surface, x, y, fill_color):
    """Simple queue-based flood fill"""
    if x < 0 or x >= WIDTH or y < CANVAS_Y or y >= HEIGHT:
        return
    target_color = surface.get_at((x, y))
    if target_color == fill_color:
        return

    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if not (0 <= cx < WIDTH and CANVAS_Y <= cy < HEIGHT):
            continue
        if surface.get_at((cx, cy)) != target_color:
            continue

        surface.set_at((cx, cy), fill_color)
        stack.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])

# ====================== MAIN LOOP ======================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ================= MOUSE DOWN =================
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            clicked_ui = False

            # Color palette
            for color, rect in palette:
                if rect.collidepoint(event.pos):
                    current_color = color
                    eraser_mode = False
                    clicked_ui = True

            # Tool buttons
            if eraser_button.collidepoint(event.pos):
                eraser_mode = True
                pencil_mode = line_mode = fill_mode = text_mode = False
                clicked_ui = True

            elif line_button.collidepoint(event.pos):
                line_mode = True
                pencil_mode = eraser_mode = fill_mode = text_mode = False
                clicked_ui = True

            elif fill_button.collidepoint(event.pos):
                fill_mode = True
                pencil_mode = line_mode = eraser_mode = text_mode = False
                clicked_ui = True

            elif text_button.collidepoint(event.pos):
                text_mode = True
                pencil_mode = line_mode = eraser_mode = fill_mode = False
                clicked_ui = True

            # Size buttons
            for i, btn in enumerate(size_buttons):
                if btn.collidepoint(event.pos):
                    brush_index = i
                    clicked_ui = True

            # Shape buttons (existing)
            if rectangle_button.collidepoint(event.pos):
                rectangle_mode = True
                clicked_ui = True
            # ... (other shape buttons - same as before)

            if not clicked_ui and my > CANVAS_Y:
                start_pos = event.pos

                if fill_mode:
                    flood_fill(screen, mx, my, current_color)
                elif text_mode:
                    text_pos = (mx, my)
                    text_input = ""
                elif pencil_mode or eraser_mode:
                    drawing = True
                    last_pos = event.pos
                else:
                    # Shape tools (line, rect, etc.)
                    pass

        # ================= MOUSE UP =================
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if start_pos and (line_mode or rectangle_mode or circle_mode or 
                            square_mode or right_triangle_mode or 
                            equilateral_triangle_mode or rhombus_mode):
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Line Tool
                if line_mode:
                    thickness = brush_sizes[brush_index] if not eraser_mode else 20
                    pygame.draw.line(screen, current_color if not eraser_mode else WHITE,
                                   start_pos, end_pos, thickness)

                # Other shapes (same as before - rectangle, circle, etc.)
                elif rectangle_mode:
                    # ... your existing rectangle code
                    pass
                # (Add your other shape drawing code here as before)

            drawing = False
            last_pos = None
            start_pos = None

        # ================= MOUSE MOTION =================
        if event.type == pygame.MOUSEMOTION:
            if drawing and (pencil_mode or eraser_mode):
                current_pos = event.pos
                color = WHITE if eraser_mode else current_color
                size = 20 if eraser_mode else brush_sizes[brush_index]
                pygame.draw.line(screen, color, last_pos, current_pos, size)
                last_pos = current_pos

        # ================= KEYBOARD =================
        if event.type == pygame.KEYDOWN:
            if text_mode and text_pos:
                if event.key == pygame.K_RETURN:
                    if text_input:
                        text_surf = font.render(text_input, True, current_color)
                        screen.blit(text_surf, text_pos)
                    text_mode = False
                    text_input = ""
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

            # Brush size shortcuts
            if event.key == pygame.K_1:
                brush_index = 0
            elif event.key == pygame.K_2:
                brush_index = 1
            elif event.key == pygame.K_3:
                brush_index = 2

            # Save with Ctrl+S
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"paint_{timestamp}.png"
                pygame.image.save(screen, filename)
                print(f"✅ Saved as {filename}")

    # ====================== DRAW UI ======================
    screen.fill(WHITE, (0, 0, WIDTH, CANVAS_Y))  # Clear toolbar

    # Palette
    for color, rect in palette:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Tool buttons
    buttons = [
        (eraser_button, "Eraser"),
        (line_button, "Line"),
        (fill_button, "Fill"),
        (text_button, "Text"),
    ]

    for btn, text in buttons:
        pygame.draw.rect(screen, GRAY, btn)
        pygame.draw.rect(screen, BLACK, btn, 2)
        txt = font.render(text, True, BLACK)
        screen.blit(txt, (btn.x + 5, btn.y + 10))

    # Brush size buttons
    sizes = ["S", "M", "L"]
    for i, btn in enumerate(size_buttons):
        color = (100, 200, 100) if i == brush_index else GRAY
        pygame.draw.rect(screen, color, btn)
        pygame.draw.rect(screen, BLACK, btn, 2)
        txt = small_font.render(sizes[i], True, BLACK)
        screen.blit(txt, (btn.x + 15, btn.y + 12))

    # Shape buttons (keep your existing ones)
    # ... render rectangle, circle, square, triangles, rhombus buttons

    # Live preview for Line tool
    if line_mode and start_pos and pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        thickness = brush_sizes[brush_index]
        pygame.draw.line(screen, current_color, start_pos, (mx, my), thickness)

    # Text preview
    if text_mode and text_pos and text_input:
        preview = font.render(text_input + "|", True, current_color)
        screen.blit(preview, text_pos)

    pygame.display.update()