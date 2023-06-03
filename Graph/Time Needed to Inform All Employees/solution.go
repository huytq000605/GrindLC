package main

type employee []int

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	managers := make(map[int]employee) // create a map for fast lookup to all employees of a manager
	for idx, managerID := range manager {
		if _, ok := managers[managerID]; !ok {
			managers[managerID] = employee{}
		}
		managers[managerID] = append(managers[managerID], idx)
	}
	return helper(informTime[headID], headID, &managers, &informTime)
}

// current is value to inform headID
// helper function return time to inform all employees of manager has id = headID

func helper(current int, headID int, managers *map[int]employee, informTime *[]int) int {
	max := 0
	if _, ok := (*managers)[headID]; ok { // If this manager has employees
		for _, e := range (*managers)[headID] { // Loop through all employees
			timeToInform := helper((*informTime)[e], e, managers, informTime)
			if timeToInform > max {
				max = timeToInform
			}
		}
	}

	return current + max
}
