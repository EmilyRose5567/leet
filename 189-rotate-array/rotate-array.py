class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        newnums = []
        for x in range (0,len(nums)):
            newnums.append(nums[(x - k) % len(nums)]) 
        nums[:] = newnums
        