class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dup = False
        dupped = False
        count = 0
        arr_c = arr.copy()
        for i in range(len(arr)):
            if dup:
                arr[i] = arr[i-1]
                dup = False
                dupped = True
            else:
                arr[i] = arr_c[i - count]
                dupped = False
            if arr[i] == 0 and not dupped:
                count += 1
                dup = True