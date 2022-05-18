import queue

class Solution:
    def maxSlidingWindow(self, nums , k: int) :

        res = []

        que = []

        for i in nums:
            if len(que) < k  :
                que.append(i)

                if len(que) == k :
                    res.append(max(que))
                    que.pop(0)
                
        return res


nums = [1]
k = 1

s1 = Solution()

print(s1.maxSlidingWindow(nums,k))