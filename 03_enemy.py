
import pygame
import math

class Player:
    def __init__(self):
        self.position = (0, 0)
        self.speed = 10
        self.health = 100
        self.move_x = 0
        self.move_y = 0

    def draw(self, surface):
        (dim_x, dim_y) = pygame.Surface.get_size(surface)
        print(f"dim_x: {dim_x}, dim_y: {dim_y}")
        screenspace_coords = ((self.position[0] + dim_x / 2), (self.position[1] + dim_y / 2))
        pygame.draw.circle(surface, "BLUE", screenspace_coords, 10)

    def update(self):
        length = max(math.sqrt(pow(self.move_x, 2) + pow(self.move_y, 2)), 1)
        normalized = (self.move_x / length, self.move_y / length)
        movement = (normalized[0] * self.speed, normalized[1] * self.speed)
        self.position = (self.position[0] + movement[0], self.position[1] + movement[1])
        

class Enemy:
    def __init__(self, position, size, damage):
        self.position = position
        self.radius = size
        self.damage = damage
        self.speed = 100 / size

    def draw(self, surface):
        (dim_x, dim_y) = pygame.Surface.get_size(surface)
        screenspace_coords = ((self.position[0] + dim_x / 2), (self.position[1] + dim_y / 2))
        pygame.draw.circle(surface, "RED", screenspace_coords, self.radius)

    def update(self, player, clock):
        player_pos = player.position
        direction = (player_pos[0] - self.position[0], player_pos[1] - self.position[1])
        length = max(math.sqrt(pow(direction[0], 2) + pow(direction[1], 2)), 1)
        if length >= 5:
            normalized = (direction[0] / length, direction[1] / length)
            movement = (normalized[0] * self.speed, normalized[1] * self.speed)
            self.position = (self.position[0] + movement[0], self.position[1] + movement[1])
        else:
            player.health -= self.damage * clock.get_time() / 1000
        

pygame.init()

player = Player()

enemy = Enemy((100, 100), 12, 10)

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exiting")
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("UP")
                player.move_y = -clock.get_time() * 0.1
            if event.key == pygame.K_s:
                print("DOWN")
                player.move_y = clock.get_time() * 0.1
            if event.key == pygame.K_a:
                print("LEFT")
                player.move_x = -clock.get_time() * 0.1
            if event.key == pygame.K_d:
                print("RIGHT")
                player.move_x = clock.get_time() * 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                print("UP released")
                player.move_y = 0
            if event.key == pygame.K_s:
                print("DOWN released")
                player.move_y = 0
            if event.key == pygame.K_a:
                print("LEFT released")
                player.move_x = 0
            if event.key == pygame.K_d:
                print("RIGHT released")
                player.move_x = 0
    
    screen.fill("purple")

    player.update()
    player.draw(screen)

    enemy.update(player, clock)
    enemy.draw(screen)

    if player.health <= 0:
        print("player killed!")
        running = False

    pygame.display.flip()
    clock.tick(60)

print("outside of loop")