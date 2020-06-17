#此题待议
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_same_symbol = 0
        if dividend < 0:
            is_same_symbol += 1
            dividend = -dividend
        if divisor < 0:
            is_same_symbol += 1
            divisor = -divisor
        num = 0
        while ( dividend - divisor ) >= 0:
            num += 1
            dividend -= divisor  
        while  is_same_symbol > 0:
            is_same_symbol -= 1
            num = -num
        return num
a = Solution()
print(a.divide(-9,-3))