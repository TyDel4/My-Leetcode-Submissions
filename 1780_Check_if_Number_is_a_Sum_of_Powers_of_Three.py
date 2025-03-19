import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if self.recursiveFunction(n, 0, 0) == -1:
            return True
        return False

    def recursiveFunction(self, n: int, total: int, power: int) -> bool:
        if n == total + pow(3, power):
            return True
        if n < total + pow(3, power):
            return False
        if self.recursiveFunction(n, total + pow(3, power), power + 1) == True:
            return True
        if self.recursiveFunction(n, total, power + 1) == True:
            return True
        
        return False