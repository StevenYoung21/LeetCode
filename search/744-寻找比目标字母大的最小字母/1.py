class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:

        for i in letters:
            if i > target: return(i)

        return letters[0]



letters = ["c", "f", "j"]

target = "a"

s1 = Solution()

rseult = s1.nextGreatestLetter(letters,target)

print(rseult) 