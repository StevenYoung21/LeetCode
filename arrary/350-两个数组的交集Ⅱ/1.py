class Solution:
    def intersect(self, nums1, nums2) :
        
        len1 = len(nums1)
        len2 = len(nums2)

        nums1.sort()
        nums2.sort()

        l1 , l2 = 0, 0

        res = []

        while( l1 < len1 and l2 < len2 ):
            if nums1[l1] > nums2[l2]:
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else :
                res.append(nums1[l1])
                l1 += 1
                l2 += 1

        return res



nums1 = [1,2,2,1]

nums2 = [2,2]


s1 = Solution()
res = s1.intersect(nums1,nums2)

print(res)