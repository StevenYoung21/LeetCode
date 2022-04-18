class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:

        res = {}


        def dis(arr,x,y):
            dis = abs(arr[0]-x) + abs(arr[1]-y)
            return dis


        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                disI = dis(points[i],x,y)
                res[i] = disI

        if res == {}: return -1

        min1 = min(res.values())

        resKey = []

        for key,v in res.items():
            if v == min1:
                resKey.append(key)

        if resKey != []: 
            return resKey[0]
        else:
            return -1



x = 3
y = 4
points = [[2,3]]

s1 = Solution()

print(s1.nearestValidPoint(x,y,points))