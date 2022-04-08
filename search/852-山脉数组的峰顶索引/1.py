class Solution:
    def peakIndexInMountainArray(self, arr) -> int:

        max = 0
        length = len(arr)

        # for i in arr:
        #     if i >= max:
        #         max = i

        # return arr.index(max)

        for i in range(0,length):
            if arr[i] >= max:
                max = arr[i]
            if arr[i+1] < max:
                return i




nums = [0,10,5,2]

s1 = Solution()

rseult = s1.peakIndexInMountainArray(nums)

print(rseult) 