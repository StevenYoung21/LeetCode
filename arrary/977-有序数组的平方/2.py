
class Solution:
    def sortedSquares(self, nums ) :
        
        length = len(nums) - 1

        left = 0
        right = length

        site = length
        res = [0 for i in range(length+1)]

        while( left <= right ):
            if nums[left]**2 <= nums[right]**2:
                res[site] = nums[right]**2
                right = right - 1
            else:
                res[site] = nums[left]**2
                left = left + 1
            site = site - 1

        return res



nums =  [-4,-1,0,3,10]


s1 = Solution()

rseult = s1.sortedSquares(nums)

print(rseult) 