

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while(k>0):
            nums.insert(0, nums.pop())
            k = k-1

        return nums






nums = [1]
k = 0


s1 = Solution()
res = s1.rotate(nums,k)

print(res)