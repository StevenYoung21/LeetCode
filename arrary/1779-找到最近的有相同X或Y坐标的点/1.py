class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:

        res = []


        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                res.append(points[i])

        if res == [] : return -1

        def dis(arr,x,y):

            dis = abs(arr[0]-x) + abs(arr[1]-y)

            return dis

        DisArr = []
        for i in res:
            DisArr.append(dis(i,x,y))

        minDis = min(DisArr)

        indexArr = []
        for i in range(len(DisArr)):
            if minDis == DisArr[i]:
                indexArr.append(i)

        reslutArr = []    
        for i in indexArr:
            reslutArr.append(res[i])

        indexArr2 = []
        minSum = []
        for i in reslutArr:
            minSum.append(sum(i))

        minIndex = min(minSum)

        for i in range(len(minSum)):
            if minSum[i] == minIndex:
                indexArr2.append(i)

        lastArr = reslutArr[indexArr2[0]]

        for l in range(len(points)):
            if points[l] == lastArr:
                return l

        return -1



x = 3
y = 4
points = [[3,4]]

s1 = Solution()

print(s1.nearestValidPoint(x,y,points))