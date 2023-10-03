def canPlaceFlowers(flowerbed, n):

    """
    The function takes two inputs: a list of integers representing a flowerbed and an integer n.
    The function returns True if it is possible to plant n flowers in the flowerbed, and False otherwise.
    The function works by first adding a 0 to the beginning and end of the flowerbed. This is done to ensure
    that the function can handle cases where the user wants to plant a flower at the beginning or end of the flowerbed.
    """

    # I added 0 in the begging and in the end incase there a 0 in the actual list
    f = [0] + flowerbed + [0]
    for i in range(1, len(f) - 1):
        if f[i] == 0 and f[i + 1] == 0 and f[i - 1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0


if __name__ == '__main__':

    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))
    # True
