def isPathCrossing(path):
    paths = {
        'N': [1, 0],
        'S': [-1, 0],
        'E': [0, 1],
        'W': [0, -1]
    }
    visited = set()
    x, y = 0, 0

    for p in path:
        visited.add((x, y))
        dx, dy = paths[p]
        x, y = x + dx, y + dy

        if (x, y) in visited:
            return True

    return False


if __name__ == "__main__":
    path = "NESWW"
    print(isPathCrossing(path))
    # True