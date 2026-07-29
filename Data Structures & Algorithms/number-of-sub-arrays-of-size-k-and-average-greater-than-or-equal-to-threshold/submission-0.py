class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = left + k
        res = 0
        while left <= len(arr) and right <= len(arr):
            sub_arr = arr[left : right]
            # print(sub_arr)
            sub_arr_avg = sum(sub_arr) // k
            # print(sub_arr_avg)
            if sub_arr_avg >= threshold:
                res += 1
            left += 1
            right += 1
        return res