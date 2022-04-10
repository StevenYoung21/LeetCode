from tkinter import E


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:

        l , r = 0 , len(letters) - 1

        # if target >= letters[-1] : return target[0]

        while( l <= r ):
            mid = l + ( r - l ) // 2
            if letters[mid] > target :
                r = mid - 1
            else: 
                l = mid + 1
        
        if l == len(letters):
            return letters[0]
        else:
            return letters[l]

        # return letters[ l %  len(letters) ]

        '''
        当 l == len 时:  l%len = 0
        当 l <  len 时, l%len = l
 
        '''



letters = ["c","f","j"]

target = "j"

s1 = Solution()

rseult = s1.nextGreatestLetter(letters,target)

print(rseult) 