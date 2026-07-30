class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        # print(map)
        res = 0
        for i in nums:
            local_res = 1
            if i - 1 not in map:
                while i + 1 in map:
                    # print(i, local_res)
                    local_res += 1
                    i += 1
                res = max(res, local_res)
                
        return res
