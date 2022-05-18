import queue

class Solution:
    def maxSlidingWindow(self, nums , k: int) :

        res = []
        q1 = []

        for i in range(len(nums)):
            if q1 and q1[0] == i - k:
                q1.pop(0)

            while q1 and nums[q1[-1]] < nums[i]:
                q1.pop()

            q1.append(i)

            if i >= k - 1:
                res.append(nums[q1[0]])
                
        return res


nums = [7,2,4]
k = 2

s1 = Solution()

print(s1.maxSlidingWindow(nums,k))