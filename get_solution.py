def translateMoves(solution):
    moves = ''
    positions = ['D','F','U','B','L','R']
    for i in range(len(solution)):
        if solution[i] == ' ' or solution[i] == '"' or solution[i] == '\'' or solution[i] == '2':
            continue
        else:
            moves, positions = read_move(moves, solution[i], positions)
            if i + 1 == len(solution):
                moves += 't'
                continue
            if solution[i + 1] == ' ':
                moves += 't'
                continue
            if solution[i + 1] == '\'':
                moves += 'T'
                continue
            if solution[i + 1] == '2':
                moves += 's'
                continue
    return moves

def read_move(moves, letter, positions):
    for i in range(len(positions)):
        if positions[i] == letter:
            if i == 0: 
                return w1(moves, positions)
            if i == 1:
                return w2(moves, positions)
            if i == 2:
                return w3(moves, positions)
            if i == 3:
                return w4(moves, positions)
            if i == 4:
                return w5(moves, positions)
            if i == 5:
                return w6(moves, positions)
    return moves, positions

def w1(moves, positions):
    return moves, positions

def w2(moves, positions):
    aux = [positions[1], positions[2], positions[3], positions[0], positions[4], positions[5]]
    positions = aux
    moves += 'F'

    return moves, positions


def w3(moves, positions):
    aux = [positions[2], positions[3], positions[0], positions[1], positions[4], positions[5]]
    positions = aux
    moves += 'FF'

    return moves, positions


def w4(moves, positions):
    aux = [positions[3], positions[2], positions[1], positions[0], positions[5], positions[4]]
    positions = aux
    moves += 'SF'

    return moves, positions


def w5(moves, positions):
    aux = [positions[4], positions[2], positions[5], positions[0], positions[3], positions[1]]
    positions = aux
    moves += 'rF'

    return moves, positions


def w6(moves, positions):
    aux = [positions[5], positions[2], positions[4], positions[0], positions[1], positions[3]]
    positions = aux
    moves += 'RF'

    return moves, positions
