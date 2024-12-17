# https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        datalist = []
        while n != 1:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit*digit
                n = n // 10
            if total in datalist:
                return False
            datalist.append(total)
            n = total
        return True

# https://leetcode.com/problems/power-of-two/

import math

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        log_value = math.log(n, 2)
        return abs(log_value - round(log_value)) < 1e-10  # Tolerance check

# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for n in t:
            if n in s:
                s=s.replace(n, "", 1)
                continue
            else:
                return False
        return True

# https://leetcode.com/problems/ugly-number/

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            if n != 1:
                q, r = divmod(n, 2)
                if r == 0:
                    n = q
                else:
                    break
            else:
                return True
        while True:
            if n != 1:
                q, r = divmod(n, 3)
                if r == 0:
                    n = q
                else:
                    break
            else:
                return True
        while True:
            if n != 1:
                q, r = divmod(n, 5)
                if r == 0:
                    n = q
                else:
                    return False
            else:
                return True


# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[non_zero] = nums[n]
                non_zero += 1

        for i in range(non_zero, len(nums)):
            nums[i] = 0 
            
        return nums

# https://leetcode.com/problems/reverse-vowels-of-a-string/

# https://leetcode.com/problems/third-maximum-number/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = None
        m2 = None
        m3 = None
        for n in nums:
            if n > m1:
                m3 = m2
                m2 = m1
                m1 = n
            elif n < m1 and n > m2:
                m3 = m2
                m2 = n
            elif n < m2 and n > m3:
                m3 = n
        
        if m3 != None:
            return m3
        else:
            return m1

# https://leetcode.com/problems/find-the-difference/

# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sumvalue = 0
        while num != 0:
            num, r = divmod(num, 10)
            sumvalue = sumvalue + r
            if num == 0 and sumvalue/10 != 0:
                num = sumvalue
                sumvalue = 0
        return sumvalue

# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/