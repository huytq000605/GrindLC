class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
		# Just sort it so after we do the task, we have max energy left
        tasks.sort(key = lambda task: task[1] - task[0], reverse = True)
        result = 0
        energy = 0
        n = len(tasks)
        for i in range(n):
            if energy < tasks[i][1]:
                result += tasks[i][1] - energy
                energy = tasks[i][1]
            energy -= tasks[i][0]
        return result