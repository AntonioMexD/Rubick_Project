class RubiksCube:
    def __init__(self, file_path=None):
        if file_path:
            self.load_state(file_path)
        else:
            # Initialize the cube state here
            self.cube_state = {
                'up': [['white']*3 for _ in range(3)],
                'front': [['green']*3 for _ in range(3)],
                'left': [['orange']*3 for _ in range(3)],
                'right': [['red']*3 for _ in range(3)],
                'down': [['yellow']*3 for _ in range(3)],
                'back': [['blue']*3 for _ in range(3)]
            }

    def generate_moves(self):
        return ['U', 'U\'', 'F', 'F\'', 'R', 'R\'', 'L', 'L\'', 'B', 'B\'', 'D', 'D\'']

    def parse_move(self, move):
        # Check if the move is a prime move
        prime = move.endswith("'")

        # Get the face name
        face = move.rstrip("'")

        return face, prime

    def rotate_face(self, face, prime=False):
        # If the move is prime, rotate the face counterclockwise
        if prime:
            return [list(row) for row in zip(*face)][::-1]
        else:
            return [list(row)[::-1] for row in zip(*face)]

    def load_state(self, file_path):
        with open(file_path, 'r') as file:
            new_state = {}
            face = None
            for line in file:
                parts = line.strip().split()
                if len(parts) == 1:
                    face = parts[0].replace(':', '')
                    new_state[face] = []
                elif face:
                    new_state[face].append(parts)
            self.cube_state = new_state

    def up(self, prime=False):
        # Rotate the top face
        self.cube_state['up'] = self.rotate_face(self.cube_state['up'], prime)
        # Rotate the edges
        if not prime:
            temp = self.cube_state['front'][0]
            self.cube_state['front'][0] = self.cube_state['left'][0]
            self.cube_state['left'][0] = self.cube_state['back'][0][::-1]
            self.cube_state['back'][0] = self.cube_state['right'][0]
            self.cube_state['right'][0] = temp[::-1]
        else:
            temp = self.cube_state['front'][0]
            self.cube_state['front'][0] = self.cube_state['right'][0][::-1]
            self.cube_state['right'][0] = self.cube_state['back'][0]
            self.cube_state['back'][0] = self.cube_state['left'][0][::-1]
            self.cube_state['left'][0] = temp

    def front(self, prime=False):
        # Rotate the front face
        self.cube_state['front'] = self.rotate_face(self.cube_state['front'], prime)
        # Rotate the edges
        if not prime:
            temp = [row[-1] for row in self.cube_state['up']]
            self.cube_state['up'][2] = self.cube_state['left'][::-1][2]
            self.cube_state['left'][::-1][2] = [row[0] for row in self.cube_state['down']][::-1]
            self.cube_state['down'][0] = self.cube_state['right'][::-1][0][::-1]
            self.cube_state['right'][::-1][0] = temp
        else:
            temp = [row[-1] for row in self.cube_state['up']]
            self.cube_state['up'][2] = self.cube_state['right'][::-1][0]
            self.cube_state['right'][::-1][0] = [row[0] for row in self.cube_state['down']][::-1][::-1]
            self.cube_state['down'][0] = self.cube_state['left'][::-1][2][::-1]
            self.cube_state['left'][::-1][2] = temp

    def is_solved(self):
        # Check if each face is a single color
        for face in self.cube_state.values():
            if not all(cell == face[0][0] for row in face for cell in row):
                return False
        return True

    def apply_move(self, move):
        # Parse the move
        face, prime = self.parse_move(move)

        # Apply the move
        getattr(self, face)(prime)

    def undo_move(self, move):
        # Parse the move
        face, prime = self.parse_move(move)

        # Undo the move
        getattr(self, face)(not prime)
