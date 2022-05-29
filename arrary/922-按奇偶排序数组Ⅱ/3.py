from turtle import right


class Solution:
    def sortArrayByParityII(self, nums) :

    ## 交换的位置: 在偶数位遇到了奇数, 再找一个奇数位的偶数, 进行交换

        oddIndex = 1

        for evenIndex in range(0,len(nums),2):
            if nums[evenIndex] % 2 != 0 :  ## 偶数位 遇到了 奇数
                while nums[oddIndex] % 2 != 0: ## 奇数位 遇到了 偶数
                    oddIndex += 2
                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]

        return nums


nums = [4,2,5,7]

s1 = Solution()

print(s1.sortArrayByParityII(nums))