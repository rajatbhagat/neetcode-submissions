class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            while j < k:
                sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if sum == 0:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return res