
class Solution:
    def largestPerimeter(self, nums) -> int:


        sor = sorted(nums, reverse=True)       

        for i in range( len(sor) - 2 ):
            if sor[i] < sor[i+1] + sor[i+2] and sor[i+2] > sor[i] - sor[i+1]:
                return sor[i] + sor[i+1] + sor[i+2]

        return 0

'''
思路:

构成三角形的条件: 两边之和大于第三边, 两边之差小于第三边

其中, 这个第三边分别对应最长边和最短边.

设 a >= b >= c :

则要满足: a > b + c  且  c > a - b 

解题步骤:

1. 排序并反转数组, 让数组从大到小排序, 这样保证先能构成三角形的边周长最大.

2. 对数组进行遍历, 每次取的[i]位置为最大值, [i+2]位置为最小值, 由上述公式可得:
sor[i] < sor[i+1] + sor[i+2] and sor[i+2] > sor[i] - sor[i+1]
如果此时满足构成三角形的要求, 此时的边长一定是最大的. 

3. 注意遍历数组的边界, 在i遍历到倒数第三个位置即可取完所有边.

'''


nums =[1,2,2]

s1 = Solution()

print(s1.largestPerimeter(nums))

