def destCity(paths):
    s = set()
    for path in paths:
        s.add(path[0])
    for path in paths:
        if path[1] not in s:
            return path[1]

if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(destCity(paths))
    # Sao Paulo
