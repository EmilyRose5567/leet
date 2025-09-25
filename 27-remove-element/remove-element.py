class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for x in range(0,len(nums)):
            if nums[x] == val:
                counter = counter+1
        k = len(nums)-counter
        while counter > 0:
            nums.remove(val)
            counter = counter -1
        return k
        