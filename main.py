from rubicks_cube import RubiksCube

# Create a dictionary to map the notation to the functions
notation = {
    'U': lambda cube: cube.up(),
    'U\'': lambda cube: cube.up(prime=True),
    'F': lambda cube: cube.front(),
    'F\'': lambda cube: cube.front(prime=True),
    'R': lambda cube: cube.right(),
    'R\'': lambda cube: cube.right(prime=True),
    'L': lambda cube: cube.left(),
    'L\'': lambda cube: cube.left(prime=True),
    'B': lambda cube: cube.back(),
    'B\'': lambda cube: cube.back(prime=True),
    'D': lambda cube: cube.down(),
    'D\'': lambda cube: cube.down(prime=True),
}

def depth_first_search(cube, path=[], seen_states=set()):
    # Convert the cube state to a hashable format
    cube_state = str(cube.cube_state)

    # If the cube is solved, return the current path
    if cube.is_solved():
        return path

    # If we've already seen this state, return None
    if cube_state in seen_states:
        return None

    # Add the current state to the seen states
    seen_states.add(cube_state)

    # Try each possible move
    for move in cube.generate_moves():
        # Apply the move
        cube.apply_move(move)

        # Recursively search for a solution
        result = depth_first_search(cube, path + [move], seen_states)

        # If a solution was found, return the result
        if result is not None:
            return result

        # Undo the move
        cube.undo_move(move)

    # No solution was found
    return None

def main():
    # Load the cube state from a file
    #cube = RubiksCube('C:\\Otros\\Mio2\\Tasks\\Task1\\Rubick\\cube_state.txt')
    
    cube = RubiksCube('/Users/antonio/Documents/SI/SI_Taks/Rubick/cube_state.txt')

    # Find a solution
    solution = depth_first_search(cube)

    # Print the solution
    if solution is not None:
        for i, move in enumerate(solution, 1):
            print(f'Paso {i}: {move}')
        print(f'Cantidad de pasos requeridos para la resolución: {len(solution)}')
    else:
        print('No se encontró una solución')

if __name__ == "__main__":
    main()
