class Solution:
    def intersection(self, nums1, nums2):

        res = set()

        dic = {}

        for i in nums1:
            if i not in dic:
                dic[i] = 1

        for j in nums2:
            if j in dic:
                res.add(j)

        return list(res)





nums1 = [1,2,2,1]

nums2 = [2,2]


s1 = Solution()
res = s1.intersection(nums1,nums2)

print(res)