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
        """

        :param max_x: max x coord
        :param max_y: max y xoord
        :param number: number of random points
        :return: np.array of np.array [x y] coords
        """
        output = []
        for _ in range(number):
            output.append([randint(0, max_x), randint(0, max_y)])

        output.append([-10000, 10000])
        output.append([-10000, -10000])
        output.append([10000, -10000])
        output.append([10000, 10000])

        return np.array(output)

    def point_oob(xy):
        """
        Determines if point is out of bounds
        :param xy:
        :return: True if out of bounds
        """
        for coord in xy:
            if np.abs(coord) > SCREEN_HEIGHT:
                return True

    def calculate_center(regions, region_vertices, point_regions):
        """
        Calculates the centre of the regions

        :param regions:
        :param region_vertices:
        :param point_regions:
        :return:
        """
        # Need to consider edge of screen
        to_return = []
        for ind, value in enumerate(point_regions):
            region = regions[value]
            is_region_edge = True if -1 in region else False
            region_vertex_list = [region_vertices[i] for i in region if i != -1]
            # if any of region vertex list is out of bounds then we need to do some tricky stuff otherwise we do it normal
            # if any([point_oob(region_points) for region_points in region_vertex_list]):
            #     center_x =
            # else:
            center_x = np.average([vert[0] for vert in region_vertex_list])
            center_y = np.average([vert[1] for vert in region_vertex_list])
            center = [center_x, center_y]
            to_return.append(center)

        return np.array(to_return)

    def average(a, b):
        return (a + b) / 2

    def move_towards_center(point_list, centers):
        """
        moves point towards centre of region

        :param point_list:
        :param centers:
        :return:
        """
        # Exclude points that are out of bounds
        to_return = []
        for key in centers.keys():
            value = centers[key]
            point = point_list[key]
            if point_oob(point):
                continue
            new_position = [average(point[0], value[0]), average(point[1], value[1])]
            to_return.append(new_position)

        return np.array(to_return)

    def voronoi_diagram(ponts):
        voron = Voronoi(ponts)
        voron_regions = voron.regions
        voron_vertices = voron.vertices
        return voron_regions, voron_vertices, voron.point_region

    points = create_random_vectors(WIDTH, HEIGHT, 100)
    vor_regions, vor_vertices, vor_point_region = voronoi_diagram(points)

    # calculate region centers
    region_centers = calculate_center(vor_regions, vor_vertices, vor_point_region)

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
        # points = calculate_center(vor_regions, vor_vertices, vor_point_region)

        # re calculate voronoi stuff
        # vor_regions, vor_vertices, vor_point_region = voronoi_diagram(points)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()


if __name__ == '__main__':
    main()
