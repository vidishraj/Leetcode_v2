from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [-1] * (2 * n - 1)  # Fixed-length array
        used = [False] * (n + 1)  # Track used numbers
        self.solution = None  # Store the lexicographically smallest valid sequence

        def backtrack(index: int):
            if index == len(sequence):  # Base case: full sequence found
                self.solution = sequence[:]
                return True

            if sequence[index] != -1:  # Skip already filled positions
                return backtrack(index + 1)

            for num in range(n, 0, -1):  # Try larger numbers first (greedy approach)
                if used[num]:
                    continue

                if num == 1:  # `1` only appears once
                    sequence[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = -1
                    used[1] = False

                else:  # Numbers 2 to n appear twice
                    second_index = index + num
                    if second_index < len(sequence) and sequence[second_index] == -1:
                        sequence[index] = sequence[second_index] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        sequence[index] = sequence[second_index] = -1
                        used[num] = False

            return False  # No valid sequence found

        backtrack(0)
        return self.solution
