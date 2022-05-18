class Solution:
    def topKFrequent(self, nums, k: int) :

        dis = {}

        for i in nums:
            if i not in dis:
                dis[i] = 1
            else:
                dis[i] += 1

        dis = sorted(dis.items(),key=lambda val: val[1], reverse=True)

        res = []

        for k,v in dis[:k]:
            res.append(k)

        return res



nums = [4,1,-1,2,-1,2,3]
k = 2

s1 = Solution()

print(s1.topKFrequent(nums,k))