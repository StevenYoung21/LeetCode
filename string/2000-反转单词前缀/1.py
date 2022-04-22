class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word: return word

        length = len(word)

        end = 0

        res1 = []

        for i in range(length):
            if word[i] != ch:
                res1.append(word[i])
                end += 1
            else:
                res1.append(word[i])
                break

        res1.reverse()

        resStr = ''.join(i for i in res1) + word[end+1:]

        return resStr

    
word = "abcdefd"
ch = "d"

s1=Solution()
print(s1.reversePrefix(word,ch))