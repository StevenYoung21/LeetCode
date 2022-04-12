
from sklearn.covariance import MinCovDet


class Solution:
    def arrangeCoins(self, n: int) -> int:

        l,r = 1,n

        while( l <= r ):
            mid = l + (r-l) // 2
            if ((mid+1)*mid/2) < n :
                l = mid + 1
            elif ((mid+1)*mid/2) > n:
                r = mid - 1
            else :
                return mid

        return r


'''
二分查找:

sum = (mid+1)*mid/2

计算在mid时的前n项和, 与n做比较:

1. 当sum等于 n 时, 正好是mid的位置, 返回即可
2. 当sum大于 n 时, 说明现在所在的行是没有堆满的, 要返回mid-1, 即r


'''



n = 4

s1 = Solution()

res = s1.arrangeCoins(n)

print(res)