from re import L


class Solution:
    def peakIndexInMountainArray(self, arr) -> int:

        res = 0
        length = len(arr)

        l , r = 0 ,length-1

        while ( r >= l ):
            mid = (r-l)//2 +l
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            elif arr[mid] > arr[mid+1]:
                r = mid - 1

        return l



nums = [0,10,5,2]

s1 = Solution()

rseult = s1.peakIndexInMountainArray(nums)

print(rseult) 