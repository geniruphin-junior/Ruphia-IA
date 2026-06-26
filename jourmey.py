import pygame
import random
import math
# --- CONFIGURATION ---
WIDTH, HEIGHT = 1000, 700
TILE = 50
COLS, ROWS = WIDTH // TILE, HEIGHT // TILE
FPS = 60
NOM_SITE = "WWW.TON-SITE-REVOLUTIONNAIRE.COM"
# Couleurs
VOID = (10, 10, 15)
WALL_COLOR = (50, 60, 100)
PLAYER_COLOR = (0, 255, 200)
EXIT_COLOR = (255, 0, 150)
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
    def draw(self, sc):
        x, y = self.x * TILE, self.y * TILE
        if self.walls['top']:
            pygame.draw.line(sc, WALL_COLOR, (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(sc, WALL_COLOR, (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(sc, WALL_COLOR, (x + TILE, y + TILE), (x, y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(sc, WALL_COLOR, (x, y + TILE), (x, y), 3)
    def get_neighbors(self, grid):
        neighbors = []
        idx = lambda x, y: x + y * COLS
        if self.y > 0: neighbors.append(grid[idx(self.x, self.y - 1)])
        if self.x < COLS - 1: neighbors.append(grid[idx(self.x + 1, self.y)])
        if self.y < ROWS - 1: neighbors.append(grid[idx(self.x, self.y + 1)])
        if self.x > 0: neighbors.append(grid[idx(self.x - 1, self.y)])
       
        unvisited = [n for n in neighbors if not n.visited]
        return random.choice(unvisited) if unvisited else None
class Particle:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.life = 1.0
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
   
    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.life -= 0.02
def generate_maze():
    grid = [Cell(c, r) for r in range(ROWS) for c in range(COLS)]
    stack = []
    curr = grid[0]
    visited_count = 1
   
    while visited_count < len(grid):
        curr.visited = True
        next_c = curr.get_neighbors(grid)
        if next_c:
            next_c.visited = True
            stack.append(curr)
            # Remove walls
            dx, dy = curr.x - next_c.x, curr.y - next_c.y
            if dx == 1: curr.walls['left'] = next_c.walls['right'] = False
            elif dx == -1: curr.walls['right'] = next_c.walls['left'] = False
            if dy == 1: curr.walls['top'] = next_c.walls['bottom'] = False
            elif dy == -1: curr.walls['bottom'] = next_c.walls['top'] = False
            curr = next_c
            visited_count += 1
        elif stack:
            curr = stack.pop()
    return grid
# --- INIT ---
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 28, bold=True)
grid = generate_maze()
px, py = 0, 0
particles = []
exit_cell = (COLS-1, ROWS-1)
pulse = 0
# --- MAIN LOOP ---
run = True
while run:
    sc.fill(VOID)
    pulse += 0.1
   
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
        if e.type == pygame.KEYDOWN:
            curr = grid[px + py * COLS]
            if e.key == pygame.K_UP and not curr.walls['top']: py -= 1
            if e.key == pygame.K_DOWN and not curr.walls['bottom']: py += 1
            if e.key == pygame.K_LEFT and not curr.walls['left']: px -= 1
            if e.key == pygame.K_RIGHT and not curr.walls['right']: px += 1
    # Particules
    particles.append(Particle(px * TILE + TILE//2, py * TILE + TILE//2))
    for p in particles[:]:
        p.update()
        if p.life <= 0: particles.remove(p)
        else:
            size = int(p.life * 5)
            pygame.draw.circle(sc, (0, 200, 255), (int(p.x), int(p.y)), size)
    # Dessin Labyrinthe
    for cell in grid:
        cell.draw(sc)
    # Sortie (Animation de pulsation)
    exit_rect = (exit_cell[0]*TILE + 10, exit_cell[1]*TILE + 10, TILE-20, TILE-20)
    s_size = abs(math.sin(pulse)) * 10
    pygame.draw.rect(sc, EXIT_COLOR, exit_rect, border_radius=5)
    pygame.draw.rect(sc, (255, 255, 255), exit_rect, int(2 + s_size // 2), 5)
    # Effet Ombre (Light Mask)
    mask = pygame.Surface((WIDTH, HEIGHT))
    mask.fill((0, 0, 0))
    # Création du gradient de lumière autour du joueur
    light_radius = 150
    for i in range(light_radius, 0, -10):
        alpha = int(255 * (i / light_radius))
        pygame.draw.circle(mask, (alpha, alpha, alpha), (px*TILE + TILE//2, py*TILE + TILE//2), i)
    mask.set_colorkey((255, 255, 255)) # On garde le centre transparent
    # Inversion via BLEND_RGBA_MULT pour simuler l'obscurité
    sc.blit(mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
    # Joueur (Néon)
    pygame.draw.circle(sc, PLAYER_COLOR, (px*TILE + TILE//2, py*TILE + TILE//2), TILE//4)
   
    # HUD / UI
    text_surf = font.render(NOM