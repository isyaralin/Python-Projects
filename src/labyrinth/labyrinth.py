def parse_input():
    import argparse
    import sys
    
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=None)
    args = parser.parse_args()
    
    if args.filename is not None:
        f = open(args.filename)
    else:
        f = sys.stdin
        
    input_data = f.read().strip().split("\n")
    steps = int(input_data[0])
    maze = [list(row) for row in input_data[1:]]
    return steps, maze


def find_beast(maze):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char in directions:
                return (x, y), directions[char]


def rotate_right(direction):
    dx, dy = direction
    return -dy, dx


def rotate_left(direction):
    dx, dy = direction
    return dy, -dx


def is_within_bounds(x, y, maze):
    return 0 <= y < len(maze) and 0 <= x < len(maze[0])


def simulate_beast(steps, maze):
    position, direction = find_beast(maze)
    direction_symbols = {(0, -1): '^', (0, 1): 'v', (-1, 0): '<', (1, 0): '>'}

    for _ in range(steps):
        x, y = position
        dx, dy = direction
        
        
        right_direction = rotate_right(direction)
        left_direction = rotate_left(direction)


        right_x, right_y = x + right_direction[0], y + right_direction[1]
        if is_within_bounds(right_x, right_y, maze) and maze[right_y][right_x] == '.':
            direction = right_direction
            maze[y][x] = '.'  
            x, y = position
            maze[y][x] = direction_symbols[direction] 
            for row in maze:
                print(''.join(row))
            print()  
            continue  

      
        forward_x, forward_y = x + dx, y + dy
        if is_within_bounds(forward_x, forward_y, maze) and maze[forward_y][forward_x] == '.':
            position = (forward_x, forward_y)  
            maze[y][x] = '.'  
            x, y = position
            maze[y][x] = direction_symbols[direction]  
            for row in maze:
                print(''.join(row))
            print()  
            continue  

        
        direction = left_direction
        maze[y][x] = '.'  
        x, y = position
        maze[y][x] = direction_symbols[direction]  

        for row in maze:
            print(''.join(row))
        print()  


if __name__ == "__main__":
    steps, maze = parse_input()
    simulate_beast(steps, maze)
