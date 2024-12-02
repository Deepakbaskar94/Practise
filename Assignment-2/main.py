# 1. https://leetcode.com/problems/richest-customer-wealth

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []
        for account in accounts:
            total = 0
            for n in range(len(account)):
                total += account[n]
            wealth.append(total)

        high = wealth[0]
        for data in range(len(wealth)):
            if wealth[data] > high:
                high = wealth[data]
        
        return high


                
        


# 2. https://leetcode.com/problems/running-sum-of-1d-array/
# 3. https://leetcode.com/problems/jewels-and-stones
# 4. https://leetcode.com/problems/minimum-absolute-difference
# 5. https://leetcode.com/problems/three-consecutive-odds
# 6. https://leetcode.com/problems/transpose-matrix
# 7. https://leetcode.com/problems/majority-element
# 8. https://leetcode.com/problems/move-zeroes
