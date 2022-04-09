
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 : return 0

        length = len(s)

        cur = []
        maxLen = 0

        for right in range(length):

            if s[right] not in cur:
                cur.append(s[right])
                maxLen = max(maxLen, len(cur))
            else:
                while(1): # 不知道第几个是s[right],所以让它一直运行,后面用找到了用break跳出循环
                    if s[right] != cur[0]: # 不是该元素,则删除
                        cur.pop(0)
                    else:  #是该元素了,删除该元素,跳出循环
                        cur.pop(0) 
                        break
                cur.append(s[right]) 

        return maxLen


"""
1. 用一个数组储存当前数组的情况 cur = []
2. 用maxLen来储存cur的最大长度,即 maxLen = max(len(cur), maxLen)
3. 向右侧循环遍历

4. 判断
    4.1 如果当前元素不存在cur中, 则向cur中添加该元素,添加元素会增大maxLen,所以在这判断一下.
    4.2 如果当前元素存在cur中:
        4.2.1 从cur中的第一个位置开始寻找这个元素
        4.2.2 如果不是该元素,则删除,一直删到该元素为止
        例: abcd, 如果当前元素是b,维护的cur = abcdb, 则一直删除到前一个b,结果为cdb
    4.3 再将目前的元素添加进cur

5. 返回maxLen

"""



s = "tmmzuxt"

s1 = Solution()
res = s1.lengthOfLongestSubstring(s)

print(res)