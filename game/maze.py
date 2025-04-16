# maze.py
"""
Maze generation logic for NeuroMaze game.
"""
import random
import pygame

def generate_maze(maze_size, cell_size, start_point, end_point, difficulty_level):
    """Generate maze walls based on difficulty level."""
    walls = []
    num_walls = int(maze_size * maze_size * difficulty_level)
    for _ in range(num_walls):
        wall_x = random.randint(1, maze_size - 2)
        wall_y = random.randint(1, maze_size - 2)
        wall = pygame.Rect(wall_x * cell_size, wall_y * cell_size, cell_size, cell_size)
        # Avoid walls on the start or end point
        if wall != start_point and wall != end_point:
            walls.append(wall)
    return walls
