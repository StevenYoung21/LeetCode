class Solution:
    def findKthPositive(self, arr, k: int) -> int:

        res =[]

        l = 1

        while k > 0 :
            if l not in arr:
                res.append(l)
                k -= 1
            l += 1

        return res[-1]



arr = [1,2,3,4]
k = 2

s1 = Solution()

rseult = s1.findKthPositive(arr,k)

print(rseult)