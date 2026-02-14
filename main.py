# import the pygame-ce package
import pygame

# initialize pygame
pygame.init()

# create the screen surface
screen = pygame.display.set_mode((500, 500))
# optional (for the end of the video): create clock to limit to 60 fps
clock = pygame.time.Clock()

# best option for later cleanup: global running variable
running = True

# game loop
while running:
    # iterate over events (mention events like mouse input or keyboard input)
    for event in pygame.event.get():
        # if one of the events is quit: quit
        if event.type == pygame.QUIT:
            print("exiting")
            running = False
    
    # running logic
    
    # fill the screen with purple
    screen.fill("purple")

    # dont use this at first; show later that the display needs to manually be updated (and maybe explain why)
    pygame.display.flip()

    # optional: limit to 60 fps (or anything else?)
    clock.tick(60)

# show how this is ran only after running is set to false
print("outside of loop")