class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        right = left + 1
        while left < len(nums) and right < len(nums):
            if nums[left] == nums[right]:
                return True
            else:
                right += 1
            if abs(left - right) > k:
                left += 1
                right = left + 1     
        return False
