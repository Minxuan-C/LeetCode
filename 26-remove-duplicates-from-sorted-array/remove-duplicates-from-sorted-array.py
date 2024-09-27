class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        shift = 0
        length = len(nums)
        for i in range(1, length):
            while i + shift < length and nums[i + shift] == nums[i + shift - 1]:
                shift += 1
            if i + shift < length: 
                nums[i] = nums[i + shift]
        return length - shift
                