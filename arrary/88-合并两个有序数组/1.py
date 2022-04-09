class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        len1 = len(nums1)
        len2 = len(nums2)

        for i in range(m,len1):
            nums1[i] = nums2[i-m]
            print(m,i)

        nums1.sort()

        return nums1


nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1 = [1,2,4,5,6,0]
# m = 5
# nums2 = [3]
# n = 1



s1 = Solution()
res = s1.merge(nums1,m,nums2,n)

print(res)