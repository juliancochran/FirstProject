import random
import pygame

''' 
FirstPygame project/lab, a square chasing game
__author__ Julian Cochran
__date__ 1.15.2026
'''

def main():
    # symbolic constants
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    # Before the loop: create speed variables
    speed_x = 0
    speed_y = 0
    while speed_x == 0 or speed_y == 0:
        speed_x = random.randint(-2, 2)
        speed_y = random.randint(-2, 2)
    size = (1000, 800)
    # clock controls frame rate
    clock = pygame.time.Clock()

    # intialize the Pygame engine
    pygame.init()

    # setup the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("** SQUAREMANIACZ **")
    # keep the animation loop going
    running = True
    # this is a Rect object in Pygame -- draw to the screen
    # mainRect is the game state object, it will show up in a random spot on the screen
    mainRect = pygame.Rect(random.randint(0, size[0] - 100), random.randint(0, size[1] - 100), 100, 100)
    # playerRect is the pursuing rectangle, it always starts in the middle
    playerRect = pygame.Rect((size[0] - 30) / 2, (size[1] - 30) / 2, 20, 20)

    # main animation loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # move the playerRect around the screen based on keys pressed
        # this command returns a list filled with booleans
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerRect.move_ip(-1, 0)
        if keys[pygame.K_RIGHT]:
            playerRect.move_ip(1, 0)
        if keys[pygame.K_UP]:
            playerRect.move_ip(0, -1)
        if keys[pygame.K_DOWN]:
            playerRect.move_ip(0, 1)
        # Prevent playerRect from leaving the screen
        playerRect.clamp_ip(screen.get_rect())

        # 0-255 2^8 = RGB 0000 0000 1111 1111
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, mainRect)
        pygame.draw.rect(screen, RED, playerRect)

        # updates/refreshes the display now that everything has been drawn to the screen
        pygame.display.flip()
        # Update position (move the rect)
        mainRect.x += speed_x
        mainRect.y += speed_y

        # keep mainRect on the screen, done mathematically
        if mainRect.x > size[0] - 100 or mainRect.x < 0:
            speed_x *= -1
        if mainRect.y > size[1] - 100 or mainRect.y < 0:
            speed_y *= -1

        clock.tick(180)  # 180 FPS

        if mainRect.colliderect(playerRect):
            running = False
            # break or quit the first while loop

    # closing window with goodbye text
    running = True
    font = pygame.font.Font(None, 62)  # None = default font, 36 = size
    text_surface = font.render("GAME OVER, CLICK TO QUIT", True, RED)
    text_rect = text_surface.get_rect(center=(size[0] // 2, size[1] // 2))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        screen.fill(BLACK)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
