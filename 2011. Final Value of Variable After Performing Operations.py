from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0

        total -= operations.count("--X")
        total -= operations.count("X--")
        total += operations.count("++X")
        total += operations.count("X++")

        return total
    