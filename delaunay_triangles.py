import pygame
import numpy as np

from scipy.spatial import Delaunay
from random import randint


def main():
    HEIGHT = 600
    WIDTH = 600
    pygame.init()

    SCREEN_WIDTH = HEIGHT
    SCREEN_HEIGHT = WIDTH

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Delaunay Triangles')

    RADIUS = 2

    def create_random_vectors(max_x, max_y, number):
        output = []
        for _ in range(number):
            output.append([randint(0, max_x), randint(0, max_y)])

        return np.array(output)

    points = create_random_vectors(WIDTH, HEIGHT, 500)
    tri = Delaunay(points)
    triangles = points[tri.simplices]

    run = True
    while run:
        screen.fill((255, 255, 255))

        for triangle in triangles:
            pygame.draw.line(screen, color=(0, 0, 0), start_pos=triangle[0], end_pos=triangle[1])
            pygame.draw.line(screen, color=(0, 0, 0), start_pos=triangle[0], end_pos=triangle[2])
            pygame.draw.line(screen, color=(0, 0, 0), start_pos=triangle[1], end_pos=triangle[2])

        for point in points:
            pygame.draw.circle(screen, (255, 0, 0), (point[0], point[1]), radius=RADIUS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
