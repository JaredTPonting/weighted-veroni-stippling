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

    def calculate_center(regions, region_vertices, point_regions):
        to_return = {}
        for ind, value in enumerate(point_regions):
            region = regions[value]
            if -1 in region:
                continue
            region_vertex_list = [region_vertices[i] for i in region]
            center_x = np.average([vert[0] for vert in region_vertex_list])
            center_y = np.average([vert[1] for vert in region_vertex_list])
            center = [center_x, center_y]
            to_return[ind] = center

        return to_return

    def average(a, b):
        return (a + b) / 2

    def move_towards_center(point_list, centers):
        to_return = []
        for key in centers.keys():
            value = centers[key]
            point = point_list[key]
            new_position = [average(point[0], value[0]), average(point[1], value[1])]
            to_return.append(new_position)

        return np.array(to_return)

    def voronoi_diagram(ponts):
        voron = Voronoi(ponts)
        voron_regions = voron.regions
        voron_vertices = voron.vertices
        return voron_regions, voron_vertices, voron.point_region

    points = create_random_vectors(WIDTH, HEIGHT, 5000)
    vor_regions, vor_vertices, vor_point_region = voronoi_diagram(points)

    run = True
    while run:
        screen.fill((255, 255, 255))

        # draw regions
        for v in vor_regions:
            if -1 in v:
                # -1 is a given index for voronoi vertex if the vertex does not exist in voronoi verticies. Not sure
                # how to get around this
                continue
            for ind, _ in enumerate(v):
                pygame.draw.line(screen, color=(0, 0, 0), start_pos=vor_vertices[v[ind]],
                                 end_pos=vor_vertices[v[(ind + 1) % len(v)]])

        # draw points
        for point in points:
            pygame.draw.circle(screen, (255, 0, 0), (point[0], point[1]), radius=RADIUS)

        # calculate region centers
        region_centers = calculate_center(vor_regions, vor_vertices, vor_point_region)

        # calculate move towards centers
        points = move_towards_center(points, region_centers)

        # re calculate voronoi stuff
        vor_regions, vor_vertices, vor_point_region = voronoi_diagram(points)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
