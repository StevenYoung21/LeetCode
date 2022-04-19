class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:

        arr.sort()



        a = arr[1] - arr[0]

        for i in range(len(arr)-1):
            if arr[i] + a != arr[i+1]:
                return False

        return True



arr = [2,5,1]

s1 = Solution()

print(s1.canMakeArithmeticProgression(arr))