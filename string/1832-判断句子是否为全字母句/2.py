

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        length = len(sentence)

        if length < 26 : return False

        res = set(sentence)

        if len(res) == 26 : return True
        else:  return False


sentence = "thequickbrownfoxmpsoverthelazydog"

s1 = Solution()
print(s1.checkIfPangram(sentence))