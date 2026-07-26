import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijk(start):
            pq = []
            heapq.heappush(pq, (0, start))

            dist = [float('inf')] * n
            dist[start] = 0

            ways = [0] * n
            ways[start] = 1

            while pq:
                dis, ele = heapq.heappop(pq)

                if dis > dist[ele]:
                    continue

                for nei, wei in adj[ele]:
                    cost = dis + wei

                    if cost < dist[nei]:
                        dist[nei] = cost
                        ways[nei] = ways[ele]
                        heapq.heappush(pq, (cost, nei))

                    elif cost == dist[nei]:
                        ways[nei] = (ways[nei] + ways[ele]) % MOD

            return ways[n - 1]

        return dijk(0)