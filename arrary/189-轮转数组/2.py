
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        a = 0

        while(k>0):
            a = nums.pop()
            nums.insert(0,a)
            k = k - 1

        return nums






nums = [1,2,3,4,5,6,7]
k = 3


s1 = Solution()
res = s1.rotate(nums,k)

print(res)