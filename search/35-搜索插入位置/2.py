class Solution:
    def searchInsert(self, nums, target: int) -> int:

        length = len(nums)

        l = 0
        r = length - 1

    ## 头、尾        
        if nums[0] > target : return 0
        if nums[length-1] < target :return length

        while l <= r:
            mid = (r-l)//2 + l
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target :
                r = mid - 1
            elif nums[mid] == target: 
                return mid
        
        return l

        
            






[1,3,5,6]

nums = [1,3,5,6]
  
target = 2

s1 = Solution()

rseult = s1.searchInsert(nums, target)

print(rseult) 