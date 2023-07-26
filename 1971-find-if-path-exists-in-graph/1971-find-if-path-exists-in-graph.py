class Solution:
    def dfs(self, graph, visited, current, end):
        if current == end:
            return True
        if visited[current]:
            return False
        visited[current] = 1
        for i in range(len(graph[current])):
            if self.dfs(graph, visited, graph[current][i], end):
                return True
        return False
    def validPath(self, n, edges, start, end):
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [0] * n
        return self.dfs(graph, visited, start, end)
