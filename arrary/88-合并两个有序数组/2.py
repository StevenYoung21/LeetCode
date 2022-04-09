from re import A
from tkinter import W


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        a = m - 1
        b = n - 1

        c = len(nums1)-1

        while( a >= 0 and b >= 0):
            if nums1[a] >= nums2[b]:
                nums1[c] = nums1[a]
                a -=1
            else :
                nums1[c] = nums2[b]
                b -=1
            c -=1

        while(b>=0):
            nums1[c] = nums2[b]
            b -=1
            c -=1


        return nums1


# nums1 = [1,2,3,0,0,0]
# m = 3

# nums2 = [2,5,6]
# n = 3

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1


s1 = Solution()
res = s1.merge(nums1,m,nums2,n)

print(res)