class Solution:
    def searchRange(self, nums, target) :

        if target not in nums : return[-1,-1]

        if len(nums) == 1 and nums[0] == target : return [0,0]


        def leftIndex(nums, target):

            start = 0
            end = len(nums) - 1

            while( start <= end ):
                mid = start + ( end - start ) // 2
                if nums[mid] > target :
                    end = mid - 1
                elif nums[mid] < target :
                    start = mid + 1
                else:
                    end = mid - 1
            if nums[start] == target :
                return start
            else:
                return -1

        def rightIndex(nums, target):

            start = 0
            end = len(nums) - 1

            while( start <= end ):
                mid = start + ( end - start ) // 2
                if nums[mid] > target :
                    end = mid - 1
                elif nums[mid] < target :
                    start = mid + 1
                else:
                    start = mid + 1
            if nums[end] == target :
                return end
            else:
                return -1                

        l = leftIndex(nums,target)
        r = rightIndex(nums, target)

        return [l,r]


nums = [0]
  
target = 0

s1 = Solution()

rseult = s1.searchRange(nums, target)

print(rseult) 