import pygame
from random import randint


def main():
    HEIGHT = 600
    WIDTH = 600
    pygame.init()

    SCREEN_WIDTH = HEIGHT
    SCREEN_HEIGHT = WIDTH

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Learning PyGame')

    run = True

    def create_random_vectors(max_x, max_y, number):
        output = []
        for _ in range(number):
            output.append([randint(0, max_x), randint(0, max_y)])

        return output

    points = create_random_vectors(WIDTH, HEIGHT, 1000)

    while run:
        screen.fill((255, 255, 255))

        for point in points:
            pygame.draw.circle(screen, (255, 0, 0), (point[0], point[1]), radius=1.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
