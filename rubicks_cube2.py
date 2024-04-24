class RubiksCube:
    def __init__(self, file_path=None):
        if file_path:
            self.load_state(file_path)
        else:
            # Inicializar el estado del cubo aquí
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
        # Rotar la cara en el sentido de las agujas del reloj
        if prime:
            return [list(row)[::-1] for row in zip(*face)][::-1]
        else:
            return [list(row) for row in zip(*face[::-1])]

    def load_state(self, file_path):
        try:
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
        except FileNotFoundError:
            print("El archivo especificado no se encontró.")
        except Exception as e:
            print("Error al cargar el estado del cubo:", e)
    
    def up(self, prime=False):
        # Rotar la cara superior
        self.cube_state['up'] = self.rotate_face(self.cube_state['up'], prime)
        # Rotar los bordes
        if not prime:
            temp = self.cube_state['front'][0][:]
            self.cube_state['front'][0] = self.cube_state['right'][0][:]
            self.cube_state['right'][0] = self.cube_state['back'][0][:]
            self.cube_state['back'][0] = self.cube_state['left'][0][:]
            self.cube_state['left'][0] = temp[:]
        else:
            temp = self.cube_state['front'][0][:]
            self.cube_state['front'][0] = self.cube_state['left'][0][:]
            self.cube_state['left'][0] = self.cube_state['back'][0][:]
            self.cube_state['back'][0] = self.cube_state['right'][0][:]
            self.cube_state['right'][0] = temp[:]

    def front(self, prime=False):
        # Rotar la cara frontal
        self.cube_state['front'] = self.rotate_face(self.cube_state['front'], prime)
        # Rotar los bordes
        if not prime:
            temp = self.cube_state['up'][2][:]
            self.cube_state['up'][2] = self.cube_state['left'][2][:]
            self.cube_state['left'][2] = self.cube_state['down'][0][:]
            self.cube_state['down'][0] = self.cube_state['right'][2][:]
            self.cube_state['right'][2] = temp[:]
        else:
            temp = self.cube_state['up'][2][:]
            self.cube_state['up'][2] = self.cube_state['right'][2][:]
            self.cube_state['right'][2] = self.cube_state['down'][0][:]
            self.cube_state['down'][0] = self.cube_state['left'][2][:]
            self.cube_state['left'][2] = temp[:]

    def left(self, prime=False):
        # Rotar la cara izquierda
        self.cube_state['left'] = self.rotate_face(self.cube_state['left'], prime)
        # Rotar los bordes
        if not prime:
            temp = [row[0] for row in self.cube_state['up']]
            for i in range(3):
                self.cube_state['up'][i][0] = self.cube_state['back'][2-i][2]
                self.cube_state['back'][2-i][2] = self.cube_state['down'][i][0]
                self.cube_state['down'][i][0] = self.cube_state['front'][i][0]
                self.cube_state['front'][i][0] = temp[i]
        else:
            temp = [row[0] for row in self.cube_state['up']]
            for i in range(3):
                self.cube_state['up'][i][0] = self.cube_state['front'][i][0]
                self.cube_state['front'][i][0] = self.cube_state['down'][i][0]
                self.cube_state['down'][i][0] = self.cube_state['back'][2-i][2]
                self.cube_state['back'][2-i][2] = temp[i]

    def right(self, prime=False):
        # Rotar la cara derecha
        self.cube_state['right'] = self.rotate_face(self.cube_state['right'], prime)
        # Rotar los bordes
        if not prime:
            temp = [row[2] for row in self.cube_state['up']]
            for i in range(3):
                self.cube_state['up'][i][2] = self.cube_state['front'][i][2]
                self.cube_state['front'][i][2] = self.cube_state['down'][i][2]
                self.cube_state['down'][i][2] = self.cube_state['back'][2-i][0]
                self.cube_state['back'][2-i][0] = temp[i]
        else:
            temp = [row[2] for row in self.cube_state['up']]
            for i in range(3):
                self.cube_state['up'][i][2] = self.cube_state['back'][2-i][0]
                self.cube_state['back'][2-i][0] = self.cube_state['down'][i][2]
                self.cube_state['down'][i][2] = self.cube_state['front'][i][2]
                self.cube_state['front'][i][2] = temp[i]

    def down(self, prime=False):
        # Rotar la cara inferior
        self.cube_state['down'] = self.rotate_face(self.cube_state['down'], prime)
        # Rotar los bordes
        if not prime:
            temp = self.cube_state['front'][2][:]
            self.cube_state['front'][2] = self.cube_state['right'][2][:]
            self.cube_state['right'][2] = self.cube_state['back'][0][::-1]
            self.cube_state['back'][0] = self.cube_state['left'][2][:]
            self.cube_state['left'][2] = temp[::-1]
        else:
            temp = self.cube_state['front'][2][:]
            self.cube_state['front'][2] = self.cube_state['left'][2][::-1]
            self.cube_state['left'][2] = self.cube_state['back'][0][:]
            self.cube_state['back'][0] = self.cube_state['right'][2][::-1]
            self.cube_state['right'][2] = temp[:]

    def back(self, prime=False):
        # Rotar la cara trasera
        self.cube_state['back'] = self.rotate_face(self.cube_state['back'], prime)
        # Rotar los bordes
        if not prime:
            temp = self.cube_state['up'][0][:]
            self.cube_state['up'][0] = self.cube_state['right'][0][::-1]
            self.cube_state['right'][0] = self.cube_state['down'][2][:]
            self.cube_state['down'][2] = self.cube_state['left'][0][::-1]
            self.cube_state['left'][0] = temp[:]
        else:
            temp = self.cube_state['up'][0][:]
            self.cube_state['up'][0] = self.cube_state['left'][0][::-1]
            self.cube_state['left'][0] = self.cube_state['down'][2][:]
            self.cube_state['down'][2] = self.cube_state['right'][0][::-1]
            self.cube_state['right'][0] = temp[:]
    
    def is_solved(self):
        if self.cube_state is None:
            return False
        # Check if each face is a single color
        for face in self.cube_state.values():
            if not all(cell == face[0][0] for row in face for cell in row):
                return False
        return True

    def apply_move(self, move):
        # Parse the move
        face, prime = self.parse_move(move)

        # Apply the move if it's valid
        if face in self.cube_state:
            getattr(self, face)(prime)
        else:
            print("Movimiento no válido:", move)

    def undo_move(self, move):
        # Parse the move
        face, prime = self.parse_move(move)

        # Undo the move if it's valid
        if face in self.cube_state:
            getattr(self, face)(not prime)
        else:
            print("Movimiento no válido:", move)