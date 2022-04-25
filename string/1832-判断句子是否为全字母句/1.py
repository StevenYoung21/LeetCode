

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        length = len(sentence)

        if length < 26 : return False

        res = {}

        for i in range(length):
            if sentence[i] not in res:
                res[sentence[i]] = 1
            else:
                res[sentence[i]] += 1 

        if len(res) == 26 : return True
        else:  return False


sentence = "thequickbrownfoxjumpsoverthelazydog"

s1 = Solution()
print(s1.checkIfPangram(sentence))