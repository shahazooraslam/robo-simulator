# robot_navigation.py

def move_robot(commands, start_position=(0, 0, 'S')):
    grid_rows, grid_cols=5,4
    # Define direction vectors
    directions = ['N', 'E', 'S', 'W']
    movement = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    
    # Initial position and direction
    x, y, direction = start_position
    
    for command in commands:
        if command in directions:
            # Change direction if different from current
            if command != direction:
                direction = command
        elif command == 'M':
            # Calculate potential new position
            dx, dy = movement[direction]
            new_x, new_y = x + dx, y + dy
            
            # Check boundaries
            if 0 <= new_x < grid_rows and 0 <= new_y < grid_cols:
                x, y = new_x, new_y
    
    # Return final position and direction
    return x, y, direction


if __name__ == "__main__":
    # Accept input commands
    commands = input("Enter robot commands: ").strip()
    final_position = move_robot(commands)
    print(f"Robot Location: {final_position}")
