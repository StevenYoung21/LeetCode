class Solution:
    def searchRange(self, nums, target) :

        if target not in nums : return[-1,-1]

        start = 0
        end = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == target :
                start = i
                break

        while( end > 0 ):

            if nums[end] == target:
                break

            end -= 1


        return [start,end]


nums = []
  
target = 0

s1 = Solution()

rseult = s1.searchRange(nums, target)

print(rseult) 