def findSmallestSetOfVertices(n, edges):
    indegree = [0] * n
    for edge in edges:
        indegree[edge[1]] += 1

    ans = []
    for i in range(n):
        if indegree[i] == 0:
            ans.append(i)

    return ans
    
n=5
edges=[[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]

res=findSmallestSetOfVertices(n,edges)
print(res)