class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False
        left, right = 0, length - 1
        left_k, right_k = None, None
        while left <= right and (left_k is None or right_k is None):
            if left_k is None:
                if arr[left] == arr[left + 1]:
                    return False
                elif arr[left] > arr[left + 1]:
                    left_k = left
                    print(left_k)
                left += 1
            if right_k is None:
                if arr[right] == arr[right - 1]:
                    return False
                elif arr[right] > arr[right - 1]:
                    right_k = right
                right -= 1
        print(left_k, right_k)
        if left_k == 0 or right_k == length - 1 or ((left_k is not None and right_k is not None) and left_k != right_k):
            return False
        return True 
        