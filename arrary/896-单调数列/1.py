class Solution:
    def isMonotonic(self, nums) -> bool:

        res = []
        
        def Up(nums):
            slow = 0
            fast = 1
            while fast < len(nums):
                if nums[fast] >= nums[slow]:
                    fast += 1
                    slow += 1
                else :
                    return False
            return True

        def Down(nums):
            slow = 0
            fast = 1
            while fast < len(nums):
                if nums[fast] <= nums[slow]:
                    fast += 1
                    slow += 1
                else :
                    return False
            return True 

        if Up(nums): 
            return True
        elif Down(nums):
            return True
        else:
            return False

        # return Up(nums)        

nums = [1,3,2]

s1 = Solution()

print(s1.isMonotonic(nums))