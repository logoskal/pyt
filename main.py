import pygame

WIDTH, HEIGHT = 840, 480
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
COLOR = (0, 0, 127)
BORDER_COLOR = (190, 0, 0)
WINDOW = pygame.display
FPS = 60
VEL = 5
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT,)

YELLOW_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

WIN = WINDOW.set_mode((WIDTH, HEIGHT))
WINDOW.set_caption("Game")

def draw():
    WIN.fill(COLOR)
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.update()

def yellow_movement(keys, yellow):
    keys_pressed = keys
    if keys_pressed[pygame.K_a] and yellow.x - VEL >= 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + SPACESHIP_WIDTH/1.5 <= BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL >= 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + SPACESHIP_HEIGHT <= HEIGHT:
        yellow.y += VEL

def red_movement(keys, red):
    keys_pressed = keys
    if keys_pressed[pygame.K_LEFT] and red.x - VEL - SPACESHIP_WIDTH / 6>= BORDER.x:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + SPACESHIP_WIDTH/1.5 <= WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL >= 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + SPACESHIP_HEIGHT <= HEIGHT:
        red.y += VEL

def main():
    global red
    global yellow
    red = pygame.Rect(600, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        

        draw()
        
    
    pygame.quit()

if __name__ == "__main__":
    main()