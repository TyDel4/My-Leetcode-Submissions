from typing import List
from math import sqrt

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        size_of_group = deck.count(deck[0])
        if size_of_group <= 1:
            return False
        divisors = set()
        divisors.add(size_of_group)
        temp_divisors = set()

        for i in range (2, int(sqrt(size_of_group)) + 2):
            if (size_of_group % i == 0):
                divisors.add(i)
                divisors.add(size_of_group // i)

        for i in range(1, len(deck)):
            temp_divisors = set()
            size_of_group = deck.count(deck[i])
            temp_divisors.add(size_of_group)
            for j in range (2, int(sqrt(size_of_group)) + 2):
                if (size_of_group % j == 0):
                    temp_divisors.add(j)
                    temp_divisors.add(size_of_group // j)
            divisors = divisors & temp_divisors

            if (len(divisors) <= 0):
                return False
            
            
        return True
    
sol = Solution()
print(sol.hasGroupsSizeX([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]))  # Test case