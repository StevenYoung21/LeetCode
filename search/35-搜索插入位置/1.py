class Solution:
    def searchInsert(self, nums, target: int) -> int:

        length = len(nums)

        l = 0
        r = length - 1

        while l <= r:
            mid = (r-l)//2 + l
            if nums[mid] < target:
                l = mid + 1

            elif nums[mid] > target :
                r = mid - 1

            else:
                return mid
            
        if nums[0] > target : return 0

        for i in nums:
            if i < target:
                continue
            else:
                return nums.index(i)

        return length





[1,3,5,6]

nums = [1,3,5,6]
  
target = 7

s1 = Solution()

rseult = s1.searchInsert(nums, target)

print(rseult) 