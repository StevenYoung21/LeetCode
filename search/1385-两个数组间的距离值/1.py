class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:

        def dis(a,b):
            return abs(a-b)

        len1 = len(arr1)
        len2 = len(arr2)

        k = 0

        for i in range(len1):
            m = 0
            for j in range(len2):
                if dis(arr1[i],arr2[j]) > d:
                    m = m + 1

                if( m == len2): k = k + 1
            
        return k

# 双循环暴力解法: 
# 0. 定义一个计算距离的函数, 两个数组的长度, k用来记录满足条件的次数
# 1. 外循环遍历arr1
# 2. 内循环遍历arr2
# 3. 用m记录内循环里每次距离比较大于d的次数
# 4. 如果 m == arr2 的长度，说明内循环里每次的距离都大于d, 则k++




arr1 = [1,4,2,3]
arr2 =  [-4,-3,6,10,20,30]
d = 3

s1 = Solution()

rseult = s1.findTheDistanceValue(arr1,arr2,d)

print(rseult) 