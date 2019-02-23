def translateMoves(solution):
    moves = ''
    for i in range(len(solution)):
        # print(str(i) + moves)
        # print(positions)
        if solution[i] == ' ' or solution[i] == '"' or solution[i] == '\'' or solution[i] == '2':
            continue
        else:
            moves = read_move(moves, solution[i])
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

def read_move(moves, letter):
    global positions
    for i in range(len(positions)):
        if positions[i] == letter:
            if i == 0: 
                return w1(moves)
            if i == 1:
                return w2(moves)
            if i == 2:
                return w3(moves)
            if i == 3:
                return w4(moves)
            if i == 4:
                return w5(moves)
            if i == 5:
                return w6(moves)
    # print(positions)
    # print(letter)
    return moves

def w1(moves):
    return moves

def w2(moves):
    global positions
    aux = [positions[1], positions[2], positions[3], positions[0], positions[4], positions[5]]
    positions = aux.copy()
    moves += 'F'
    return moves

def w3(moves):
    global positions
    aux = [positions[2], positions[3], positions[0], positions[1], positions[4], positions[5]]
    positions = aux.copy()
    moves += 'FF'
    return moves

def w4(moves):
    global positions
    aux = [positions[3], positions[2], positions[1], positions[0], positions[5], positions[4]]
    positions = aux.copy()
    moves += 'SF'
    return moves

def w5(moves):
    global positions
    aux = [positions[4], positions[2], positions[5], positions[0], positions[3], positions[1]]
    positions = aux.copy()
    moves += 'rF'
    return moves

def w6(moves):
    global positions
    aux = [positions[5], positions[2], positions[4], positions[0], positions[1], positions[3]]
    positions = aux.copy()
    moves += 'RF'
    return moves

positions = ['D','F','U','B','L','R']
# solution = "R2 B2 L2 U2 R F U2 D2 F U F2 L2 F2 D B2 U' F2 U' F2"
# moves = translateMoves(solution)

# print(moves)
