class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length <= 2:
            for i in range(length):
                if nums[i] == target:
                    return i
            return -1 
        else:
            left, right = 0, length - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[left] < nums[mid]:
                    if nums[left] == target:
                        return left
                    elif nums[left] < target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[right] == target:
                        return right
                    elif nums[mid] < target < nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1 
        
        
                
                    
                    
                    
                        
                
            