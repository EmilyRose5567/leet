class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(0,len(nums)):
            if i > maxReach:
                return False
            else: maxReach = max(maxReach, i + nums[i])
        return maxReach>=i




        