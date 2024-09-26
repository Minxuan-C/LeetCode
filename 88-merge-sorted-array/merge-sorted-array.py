class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:n]
        elif n == 0:
            nums1[:] = nums1[:m]
        else:
            temp1 = nums1[:m]
            temp2 = nums2[:n]
            left, right = 0,0
            for i in range(m+n):
                if right < n:
                    if left < m and temp1[left] <= temp2[right]:
                        nums1[i] = temp1[left]
                        left += 1
                    else:
                        nums1[i] = temp2[right]
                        right += 1
                else:
                    nums1[i] = temp1[left]
                    left += 1
                
                
        