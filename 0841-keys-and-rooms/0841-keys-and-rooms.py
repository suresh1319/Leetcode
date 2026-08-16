class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0]*n
        def dfs(node):
            visited[node] = 1 
            for nei in rooms[node]:
                if visited[nei] == 0:
                    dfs(nei)
        dfs(0)
        return sum(visited) == n