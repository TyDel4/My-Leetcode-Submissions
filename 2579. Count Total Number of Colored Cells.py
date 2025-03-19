class Solution:
    def coloredCells(self, n: int) -> int:
        total = 1
        for i in range(1, n):
            total += 4 * i
        return total
    