import random

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num=8, state=()):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X' + '. ' * (length - pos - 1)

    for pos in solution:
        print line(pos)

pretty_print(random.choice(list(queens(8))))
