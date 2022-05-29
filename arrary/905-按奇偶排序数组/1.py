class Solution:
    def sortArrayByParity(self, nums) :

        res = []

        for i in nums:
            if i % 2 == 0:
                res.insert(0,i)
            else:
                res.append(i)

        return res

nums = [3,1,2,4]

s1 = Solution()

print(s1.sortArrayByParity(nums))