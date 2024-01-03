def numberOfBeams(bank):
    total = 0
    prev = bank[0].count("1")

    for i in range(1, len(bank)):
        curr = bank[i].count("1")
        if curr:
            total += prev * curr
            prev = curr

    return total


if __name__ == "__main__":
    bank = ["011001", "000000", "010100", "001000"]
    print(numberOfBeams(bank))
