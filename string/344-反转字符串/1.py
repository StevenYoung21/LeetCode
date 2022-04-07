from turtle import left, right


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        length = len(s)

        temp = ['']    

        left , right = 0 , length - 1

        while(left <= right):
            # temp = s[left]
            # s[left] =  s[right]
            # s[right] = temp

            s[right] , s[left] = s[left], s[right]

            left += 1
            right -=1


        return s



s = ["h","e","l","l","o"]

s1 = Solution()
res = s1.reverseString(s)

print(res)