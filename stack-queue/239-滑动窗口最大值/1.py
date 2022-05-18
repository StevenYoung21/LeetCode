import queue

class Solution:
    def maxSlidingWindow(self, nums , k: int) :

        q1 = queue.Queue()

        res = []


        def maxNumQue(queue):
            
            res = []
            q2 = queue

            while not q2.empty():
                temp = q2.get()
                res.append(temp)

            for i in res:
                q2.put(i)

            return max(res)

        i = 0

        for ele in nums:
            if i < k:
                q1.put(ele)
                i += 1

            if i == k:
                res.append(maxNumQue(q1))
                q1.get()
                i -= 1
                
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

s1 = Solution()

print(s1.maxSlidingWindow(nums,k))