class Solution:
    def searchRange(self, nums, target) :

        if target not in nums : return[-1,-1]

        if len(nums) == 1 and nums[0] == target : return [0,0]

        start = 0
        end = len(nums) - 1

        while( start <= end ):
            mid = start + ( end - start ) // 2
            if nums[mid] > target :
                end = mid - 1
            elif nums[mid] < target :
                start = mid + 1
            else:
                break


        l = 0
        r = len(nums) -1

        res = []

        while( l <= mid or r >= mid ):

            if nums[l] != target and nums[l+1] == target  :
                res.append(l+1)

            if nums[r] != target and nums[r-1] == target :
                res.append(r-1)
            l = l + 1
            r = r - 1 

        res.sort()

        return res


        # return [start,end]


nums = [2,2]
  
target = 2

s1 = Solution()

rseult = s1.searchRange(nums, target)

print(rseult) 