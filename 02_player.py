import pygame
import math

# player class
class Player:
    # constructor
    def __init__(self):
        # default values
        self.position = (0, 0)
        self.speed = 5
        self.move_x = 0
        self.move_y = 0

    # drawing function
    def draw(self, surface):
        # get the window size, important for centering the player
        (dim_x, dim_y) = pygame.Surface.get_size(surface)
        print(f"dim_x: {dim_x}, dim_y: {dim_y}")
        screenspace_coords = ((self.position[0] + dim_x / 2), (self.position[1] + dim_y / 2))
        pygame.draw.circle(surface, "BLUE", screenspace_coords, 10)

    # update function, handles movement vector
    def update(self):
        # calculate the direction vector length
        length = max(math.sqrt(pow(self.move_x, 2) + pow(self.move_y, 2)), 1)
        # calculate the normalized direction vector
        normalized = (self.move_x / length, self.move_y / length)
        # calculate the actual movement vector by multiplying the normalized direction vector with the speed attribute
        movement = (normalized[0] * self.speed, normalized[1] * self.speed)
        # calculating the new position by adding the movement vector onto the player position
        self.position = (self.position[0] + movement[0], self.position[1] + movement[1])
        

pygame.init()

player = Player()

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

    pygame.display.flip()
    clock.tick(60)

print("outside of loop")