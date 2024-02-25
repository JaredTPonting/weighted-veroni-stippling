import pygame
import numpy as np

from scipy.spatial import Voronoi
from random import randint


def main():
    HEIGHT = 600
    WIDTH = 600
    pygame.init()

    SCREEN_WIDTH = HEIGHT
    SCREEN_HEIGHT = WIDTH

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Voronoi Diagram')

    RADIUS = 2

    def create_random_vectors(max_x, max_y, number):
        output = []
        for _ in range(number):
            output.append([randint(0, max_x), randint(0, max_y)])

        return np.array(output)

    def entropy(vertices):
        to_return = []
        for vertex in vertices:
            to_return.append([(vertex[0]+randint(-1, 1))%WIDTH, (vertex[1]+randint(-1, 1))%HEIGHT])

        return np.array(to_return)

    def voronoi_diagram(ponts):
        voron = Voronoi(ponts)
        voron_regions = voron.regions
        voron_vertices = voron.vertices
        return voron_regions, voron_vertices

    points = create_random_vectors(WIDTH, HEIGHT, 200)
    # vor = Voronoi(points)
    # vor_regions = vor.regions
    # vor_vertices = vor.vertices

    run = True
    while run:
        screen.fill((255, 255, 255))

        points = entropy(points)
        vor_regions, vor_vertices = voronoi_diagram(points)

        for v in vor_regions:
            if -1 in v:
                # -1 is a given index for voronoi vertex if the vertex does not exist in voronoi verticies. Not sure
                # how to get around this
                continue
            for ind, _ in enumerate(v):
                pygame.draw.line(screen, color=(0, 0, 0), start_pos=vor_vertices[v[ind]],
                                 end_pos=vor_vertices[v[(ind + 1) % len(v)]])

        for point in points:
            pygame.draw.circle(screen, (255, 0, 0), (point[0], point[1]), radius=RADIUS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
