from rubicks_cube2 import RubiksCube

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
    cube = RubiksCube()
    cube.load_state('/Users/antonio/Documents/SI/Rubick_Project/Rubick_Project/cube_state4.txt')

    # Verifica si el cubo está resuelto inicialmente
    if cube.is_solved():
        print("El cubo está resuelto inicialmente.")
    else:
        print("El cubo no está resuelto inicialmente.")

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