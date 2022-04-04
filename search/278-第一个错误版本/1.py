# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = (right-left)//2+left
            if(isBadVersion(mid)):
                # if(not isBadVersion(mid-1)) : return mid
                right = mid - 1
            else:
                # if(isBadVersion(mid+1)) : return mid + 1
                left = mid + 1
        return left
                

        

n = 5
bad = 4

