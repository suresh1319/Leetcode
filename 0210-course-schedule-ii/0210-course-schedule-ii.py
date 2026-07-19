class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        dq = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                dq.append(i)
        ans = []
        while dq:
            ele = dq.popleft()
            for nei in adj[ele]:
                indeg[nei]-=1
                if indeg[nei] == 0:
                    dq.append(nei)
            ans.append(ele)
        return ans if len(ans) == numCourses else []