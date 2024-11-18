import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x = 0
        y = 0
        running = True
        while running:
            mole_image_rect = mole_image.get_rect(topleft=(x,y))
            left_border = mole_image_rect[0]
            right_border = mole_image_rect[0] + mole_image_rect[2]
            top_border = mole_image_rect[1]
            bottom_border = mole_image_rect[1] + mole_image_rect[3]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] > left_border and event.pos[0] < right_border:
                        if event.pos[1] > top_border and event.pos[1] < bottom_border:
                            print("hi")
                            print(left_border, right_border, top_border, bottom_border)
                            new_position = [random.randint(0, 640), random.randint(0, 512)]
                            for i in range(len(new_position)):
                                while new_position[i] % 32 != 0:
                                    if i == 0:
                                        new_position[i] = random.randint(0, 640-32)
                                    elif i == 1:
                                        new_position[i] = random.randint(0, 512-32)
                            x = new_position[0]
                            y = new_position[1]
            screen.fill("light green")
            for i in range(1,17):
                pygame.draw.line(screen, "black", (0, 32*i), (640, 32*i))
            for j in range(1, 21):
                pygame.draw.line(screen, "black", (32*j, 0),  (32 * j, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()