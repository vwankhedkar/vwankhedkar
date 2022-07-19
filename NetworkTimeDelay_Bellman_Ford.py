not working

import math
def networkDelayTime(times, N, K):
    distances = [-1] * N
    distances[K-1] = 0
    for i in range(N - 1):
        count = 0
        for j in range(len(times)):
            source = times[j][0]
            target = times[j][1]
            weight = times[j][2]

            if (distances[source-1] + weight < distances[target-1]):
                distances[target-1] = distances[source-1]+weight
                count += 1
        if (count == 0):
            break
        print(distances)
        ans = max(distances)
        return ans
        print(distances, source, target, weight, ans) 
    
t = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6],[3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(networkDelayTime(t, 5, 1))
