
class Solution:
    def maxSlidingWindow(self, nums , k: int) :

        res = []
        q1 = []

        # q1.pop() ## 尾删
        # q1.pop(0) ## 头删

        for i in range(len(nums)):

            while q1 and nums[q1[-1]] < nums[i]:
                q1.pop()
                
            q1.append(i)

            if q1 and q1[0] == i - k:
                q1.pop(0)

            if i >= k-1:
                   res.append(nums[q1[0]])   

        return res


nums = [1,-1]
k = 1

s1 = Solution()

print(s1.maxSlidingWindow(nums,k))