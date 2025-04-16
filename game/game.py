import pygame
import random
import time
from game.maze import generate_maze
from emotion_detector.backend_client import send_to_backend

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dystopian Maze Game")

# Colors (dystopian theme)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

# Maze settings
maze_size = 10  # Number of cells in the maze (rows and columns)
cell_size = WIDTH // maze_size
player = pygame.Rect(1 * cell_size, 1 * cell_size, cell_size, cell_size)

# Difficulty settings
difficulty = "Normal"
feedback = "Waiting for AI feedback..."

# Maze structure
walls = []
start_point = pygame.Rect(
    1 * cell_size, 1 * cell_size, cell_size, cell_size
)  # Top-left
end_point = pygame.Rect(
    (maze_size - 2) * cell_size, (maze_size - 2) * cell_size, cell_size, cell_size
)  # Bottom-right


def update_maze_by_difficulty(difficulty):
    if difficulty == "Easy":
        return generate_maze(maze_size, cell_size, start_point, end_point, 0.1)
    elif difficulty == "Normal":
        return generate_maze(maze_size, cell_size, start_point, end_point, 0.3)
    elif difficulty == "Hard":
        return generate_maze(maze_size, cell_size, start_point, end_point, 0.5)
    return []


def draw_game():
    """Draw maze, player, start/end points, and UI overlays."""
    screen.fill(BLACK)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    # Draw start and end points
    pygame.draw.rect(screen, GREEN, start_point)  # Start point (green)
    pygame.draw.rect(screen, RED, end_point)  # End point (red)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw difficulty and feedback
    font = pygame.font.SysFont("Arial", 24)
    difficulty_text = font.render(f"Difficulty: {difficulty}", True, WHITE)
    feedback_text = font.render(f"Feedback: {feedback}", True, WHITE)
    screen.blit(difficulty_text, (20, 20))
    screen.blit(feedback_text, (20, 60))

    pygame.display.flip()


def is_valid_move(x, y):
    """Check if the player's next position is valid (not colliding with walls or out of bounds)."""
    # Check for collisions with walls
    new_player_rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    for wall in walls:
        if new_player_rect.colliderect(wall):
            return False

    # Ensure player doesn't move off-screen (boundary checks)
    if x < 0 or x >= maze_size or y < 0 or y >= maze_size:
        return False

    return True


def game_loop():
    """Main game loop for handling events, movement, and backend communication."""
    global player, difficulty, feedback, walls
    emotion = "Neutral"  # Starting emotion

    last_update = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Movement keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and is_valid_move(
            player.x // cell_size - 1, player.y // cell_size
        ):
            player.x -= cell_size
        if keys[pygame.K_RIGHT] and is_valid_move(
            player.x // cell_size + 1, player.y // cell_size
        ):
            player.x += cell_size
        if keys[pygame.K_UP] and is_valid_move(
            player.x // cell_size, player.y // cell_size - 1
        ):
            player.y -= cell_size
        if keys[pygame.K_DOWN] and is_valid_move(
            player.x // cell_size, player.y // cell_size + 1
        ):
            player.y += cell_size

        # Detect emotion and adjust difficulty every 3 seconds
        if time.time() - last_update > 3:
            result = send_to_backend(emotion)
            difficulty = result["difficulty"]
            feedback = result["feedback"]
            walls[:] = update_maze_by_difficulty(difficulty)
            last_update = time.time()

        # Check if player reached the end point
        if player.colliderect(end_point):
            display_win_message()

        # Draw the game with updated difficulty
        draw_game()

        pygame.display.update()


def display_win_message():
    """Display win message and exit game."""
    font = pygame.font.SysFont("Arial", 48)
    win_text = font.render("You Win!", True, PURPLE)
    screen.fill(BLACK)
    screen.blit(
        win_text,
        (
            WIDTH // 2 - win_text.get_width() // 2,
            HEIGHT // 2 - win_text.get_height() // 2,
        ),
    )
    pygame.display.flip()
    pygame.time.wait(2000)  # Show win message for 2 seconds
    pygame.quit()


if __name__ == "__main__":
    game_loop()
