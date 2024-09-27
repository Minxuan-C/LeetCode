class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 0, x-1
        nearest = -1
        while left <= right:
            mid = (left + right) //2 
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                nearest = mid
                left = mid + 1
            else:
                nearest = mid - 1
                right = mid - 1
        return nearest
                
                
            
        