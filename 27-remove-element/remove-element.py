class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift = 0
        length = len(nums)
        for i in range(length):
            while i + shift < length and nums[i + shift] == val:
                    shift += 1
            if i + shift < length:
                nums[i] = nums[i + shift]
        return length - shift
        