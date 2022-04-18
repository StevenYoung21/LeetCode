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

        mixV = float('inf')
        for value in res.values():
            mixV = min(mixV,value)

        

        return mixV



x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

s1 = Solution()

print(s1.nearestValidPoint(x,y,points))