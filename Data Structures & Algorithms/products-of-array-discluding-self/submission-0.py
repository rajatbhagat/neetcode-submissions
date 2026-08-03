class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0 for x in nums]
        post = [0 for x in nums] 
        res = [0 for x in nums]
        post[-1] = nums[-1]
        post[-2] = nums[-1]
        pre[0] = nums[0]
        pre[1] = nums[0]
        for i in range(2, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(nums) - 3, -1, -1):
            # print(post[i + 1], nums[i + 1])
            post[i] = post[i + 1] * nums[i + 1]
        res[0] = post[0]
        res[-1] = pre[-1]
        # print(pre, post)
        for i in range(1, len(nums) - 1):
            res[i] = pre[i] * post[i]
        return res