def kidsWithCandies(candies, extraCandies):

    """
    The Python function kidsWithCandies() takes an array of integers candies and an integer extraCandies as input
     and returns a boolean array of the same length as candies, where each element of the returned array indicates
     whether the corresponding kid will have the greatest number of candies among all the kids after giving them extraCandies candies.
    """

    maxNoCandies = max(candies)

    for idx, no_candie in enumerate(candies):
        candies[idx] = (no_candie + extraCandies) >= maxNoCandies
    return candies

if __name__ == "__main__":
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))
    # [True, True, True, False, True]