def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s 
    cap_x = 8 
    successor_states = []

    #Empty bottle 
    if x > 0:
        successor_states.append(((0, y, z), x))
    if y > 0:
        successor_states.append(((x, 0, z), y))
    if z > 0:
        successor_states.append(((x, y, 0), z))

    #Fill up bottle
    if x < cap_x:
        successor_states.append(((cap_x, y, z), cap_x - x))

    #Pour water
    for i in range(3):
        for j in range(3):
            if i != j:
                pour = min(s[i], cap_x - s[j])
                if pour > 0:
                    new_state = list(s)
                    new_state[i] -= pour
                    new_state[j] += pour
                    successor_states.append((tuple(new_state), pour))

    return successor_states
