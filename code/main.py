import pygame
from random import randint
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

surf = pygame.Surface((100, 200))
surf.fill('orange')

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2(20, -10)
player_speed = 10

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()  
star_positions = [(randint(0, WINDOW_WIDTH - star_surf.get_width()), randint(0, WINDOW_HEIGHT - star_surf.get_height())) 
                   for _ in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(center = (20, WINDOW_HEIGHT - 20))



while running:
    dt = clock.tick()
    print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game Screen
    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    
    # Player
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()