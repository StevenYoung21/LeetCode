class Solution:
    def average(self, salary) -> float:

        maxNum = max(salary)
        minNum = min(salary)

        ave = (sum(salary) - maxNum - minNum) / (len(salary) - 2)

        return ave




salary = [4000,3000,1000,2000]


s1 = Solution()

rseult = s1.average(salary)

print(rseult) 