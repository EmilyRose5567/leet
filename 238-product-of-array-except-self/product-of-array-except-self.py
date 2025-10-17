class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0,len(nums)):
            answer.append(1)
        prefix = 1
        for i in range(0,len(nums)):
            answer[i] = prefix
            prefix = prefix * nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i]=answer[i]*suffix
            suffix = suffix*nums[i]
        return answer

        