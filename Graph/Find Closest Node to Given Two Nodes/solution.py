class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        from_1 = [-1 for i in range(n)]
        from_2 = [-1 for i in range(n)]

        def traversal(u, arr):
            arr[u] = 0
            cur = 0
            while True:
                v = edges[u]
                if v == -1 or arr[v] != -1:
                    break
                cur += 1
                arr[v] = cur
                u = v
        traversal(node1, from_1)
        traversal(node2, from_2)

        result_distance = math.inf
        result_idx = -1
        for i in range(n):
            if from_1[i] != -1 and from_2[i] != -1 and max(from_1[i], from_2[i]) < result_distance:
                result_idx = i
                result_distance = max(from_1[i], from_2[i])
        return result_idx
