class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        There are n balls on a table, each ball has a color black or white.

        You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

        In each step, you can choose two adjacent balls and swap them.

        Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
        """
        
        # Initialize swap and black to 0
        swap, black = 0, 0
        # Iterate through the string
        for c in s:
            # If the current ball is white, add the current count of black balls to swap
            if c == '0':
                swap += black
            # If the current ball is black, increment the count of black balls
            else:
                black += 1
        # Return the total number of swaps
        return swap

if __name__ == '__main__':

    ss = "10101"
    s = Solution()
    print(s.minimumSteps(ss))