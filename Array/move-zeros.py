#Leetcode 283- Move Zeros
#two pointer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i] !=0 :
                nums[i], nums[j] = nums[j], nums[i]
                j+=1

        while j<len(nums):
            nums[j]=0
            j+=1     
