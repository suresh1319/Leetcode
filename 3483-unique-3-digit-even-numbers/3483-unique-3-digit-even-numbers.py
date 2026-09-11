class Solution:
    def totalNumbers(self, digits):
        freq = [0] * 10

        # Count frequency of each digit
        for digit in digits:
            freq[digit] += 1

        count = 0

        # Last digit must be even
        for last in range(0, 10, 2):

            if freq[last] == 0:
                continue

            freq[last] -= 1

            # First digit cannot be 0
            for first in range(1, 10):

                if freq[first] == 0:
                    continue

                freq[first] -= 1

                # Middle digit
                for middle in range(10):
                    if freq[middle] > 0:
                        count += 1

                freq[first] += 1

            freq[last] += 1

        return count