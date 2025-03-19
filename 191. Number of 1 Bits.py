class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n > 0:
            if int(n) & int(1) == 1:
                total += 1
            n /= 2

        return total
    