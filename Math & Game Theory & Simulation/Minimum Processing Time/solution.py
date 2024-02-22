class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        # 0 -> [0, 3]
        # 1 -> [4, 7]
        result = 0
        for i, s in enumerate(processorTime):
            result = max(result, s + tasks[i*4])
        return result
        
