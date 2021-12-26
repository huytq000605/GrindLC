from collections import deque
import math
from typing import *

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = []
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                for j in range(0, n):
                    arr.append(board[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    arr.append(board[i][j])
        queue = deque([[0, 0]])
        distance = [math.inf] * (n*n)
        distance[0] = 0
        while queue:
            idx, steps = queue.popleft()
            if idx == n * n - 1:
                return steps
            for i in range(1, 7):
                if idx + i >= n*n:
                    break
                if arr[idx + i] != -1 and distance[arr[idx + i] - 1] >= steps + 1:
                    distance[arr[idx + i] - 1] = steps + 1
                    queue.append([arr[idx + i] - 1, steps + 1])
                elif arr[idx+i] == -1 and distance[idx + i] >= steps + 1:
                    distance[idx + i] = steps + 1
                    queue.append([idx + i, steps + 1])
            
        return -1