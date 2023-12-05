def numberOfMatches(n):
    total_matches = 0
    teams = n

    while teams > 1:

        if teams % 2 == 0:
            total_matches += int(teams / 2)
            teams = teams / 2

        elif teams % 2 != 0:
            total_matches += int(((teams - 1) / 2))
            teams = ((teams - 1) / 2) + 1

    return total_matches


def numberOfMatches2(n):
    return 0 if n <= 1 else int(n - 1)


if __name__ == '__main__':
    n = 7
    print(numberOfMatches(n))
    # 6
    print(numberOfMatches2(n))
    # 6
