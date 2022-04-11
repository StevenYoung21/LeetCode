class Solution:
    def intersect(self, nums1, nums2) :
        
        len1 = len(nums1)
        len2 = len(nums2)

        dic = {}
        res = []

        for i in range(len1):
            if nums1[i] not in dic:
                dic[nums1[i]] = 1
            else:
                dic[nums1[i]] += 1

        for j in range(len2):
            if nums2[j] in dic and dic[nums2[j]] > 0:
                res.append(nums2[j])
                dic[nums2[j]] -=1

        return res



nums1 = [1,2,2,1]

nums2 = [2,2]


s1 = Solution()
res = s1.intersect(nums1,nums2)

print(res)