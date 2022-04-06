
class Solution:
    def twoSum(self, nums, target: int) :

        length = len(nums)

        map_a = dict()

        # for i in range(length):
        #     map_a[nums[i]] = i

        
        for i in range(length):

            index = target - nums[i]

            if index in map_a and i != map_a[index]: 
                
                return [map_a[index],i]
            map_a[nums[i]] = i        



   


nums = [2,7,11,15]
target = 9


## 哈希表

s1 = Solution()
res = s1.twoSum(nums,target)

print(res)