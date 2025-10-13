class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentEnd = 0
        maxReach = 0
        
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])
            
            if i == currentEnd:
                jumps += 1
                currentEnd = maxReach

        return jumps

        