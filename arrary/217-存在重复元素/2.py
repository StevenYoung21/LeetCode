class Solution:
    def containsDuplicate(self, nums) -> bool:

        length1 = len(nums)
        s1 = set(nums)
        length2 = len(s1)

        if length1 == length2 : return False 
        else : return True
 



nums = [1,2,3,4]


## set

s1 = Solution()
res = s1.containsDuplicate(nums)

print(res)