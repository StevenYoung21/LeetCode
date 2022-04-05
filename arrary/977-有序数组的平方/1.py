class Solution:
    def sortedSquares(self, nums ) :
        
        arr = []
        for i in nums:
            arr.append(i*i)
        arr.sort()
        return arr





nums =  [-4,-1,0,3,10]


s1 = Solution()

rseult = s1.sortedSquares(nums)

print(rseult) 