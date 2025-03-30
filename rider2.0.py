import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
car_image = pygame.image.load('CAR2.png').convert_alpha()
car_image = pygame.transform.scale(car_image, (100, 100))
coin_image = pygame.image.load('COIN2.png').convert_alpha()
coin_image = pygame.transform.scale(coin_image, (40, 40))
train_image = pygame.image.load('train2.png').convert_alpha()
train_image = pygame.transform.scale(train_image, (100, 100))

car_x, car_y = WIDTH // 2, HEIGHT - 120
car_speed = 5

train_width, train_height = 70, 100
train_x = random.randint(0, WIDTH - train_width)
train_y = -100
train_speed = 5

coin_x = random.randint(0, WIDTH - 40)
coin_y = -100
coin_speed = 3
coins_collected = 0
score = 0
speed_increase_threshold = 5  

font = pygame.font.SysFont("Verdana", 40)
font_large = pygame.font.SysFont("Verdana", 60)
game_over_text = font_large.render("Game Over", True, BLACK)

running = True
while running:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 100:
        car_x += car_speed

    train_y += train_speed
    if train_y > HEIGHT:
        train_y = -train_height
        train_x = random.randint(0, WIDTH - train_width)
        score += 1

    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -40
        coin_x = random.randint(0, WIDTH - 40)
    
    if (train_x < car_x < train_x + train_width or train_x < car_x + 100 < train_x + train_width) and \
       (train_y < car_y < train_y + train_height or train_y < car_y + 100 < train_y + train_height):
        screen.fill(RED)
        screen.blit(game_over_text, (250, 250))
        pygame.display.update()
        time.sleep(2)
        running = False
    
    if (coin_x < car_x < coin_x + 40 or coin_x < car_x + 100 < coin_x + 40) and \
       (coin_y < car_y < coin_y + 40 or coin_y < car_y + 100 < coin_y + 40):
        coins_collected += 1
        coin_y = -40
        coin_x = random.randint(0, WIDTH - 40)
        
    if coins_collected % speed_increase_threshold == 0 and coins_collected > 0:
        train_speed += 0.5
        car_speed += 0.5
        coin_speed += 0.2
        coins_collected += 1  
    
    screen.blit(car_image, (car_x, car_y))
    screen.blit(train_image, (train_x, train_y))
    screen.blit(coin_image, (coin_x, coin_y))
    score_display = font.render(f"Score: {score}", True, BLACK)
    coins_display = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_display, (600, 10))
    screen.blit(coins_display, (600, 50))

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
