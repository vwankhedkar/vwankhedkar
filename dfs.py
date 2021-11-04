managersArray = [2, 2, 4, 6, -1, 4, 4, 5]
informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0]
def numOfMinutes(n, headID, managers, informTime):
    adjList = managers.map((),[])
    for employee in range(n):
        manager = managers[employee]
        if (manager == -1):
            continue
        adjList[manager].push(employee)

    return dfs(headID, adjList, informTime)

def dfs(currentID, adjList, informTime):
    if (len(adjList[currentID]) == 0):
        return 0
    max = 0
    subordinates = adjList[currentID]
    for i in range(len(subordinates)):
        max = Math.max(max, dfs(subordinates[i], adjList, informTime))

    return max + informTime[currentID]

print(numOfMinutes(8, 4, managersArray, informTimeArray))
