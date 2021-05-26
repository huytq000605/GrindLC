package main

/*
First we let the gravity fall by each row ( mutating the box ), i mark the "ground" as the last "object" we meet.
Then we create new 2d slice result which each column of it is column of box with reverse index
*/

func rotateTheBox(box [][]byte) [][]byte {
	for i := 0; i < len(box); i++ {
		lastObj := len(box[0])
		for j := len(box[0]) - 1; j >= 0; j-- {
			if box[i][j] == '*' {
				lastObj = j
			}
			if box[i][j] == '#' {
				box[i][j] = '.'
				box[i][lastObj-1] = '#'
				lastObj = lastObj - 1
			}
		}
	}
	result := make([][]byte, len(box[0]))
	for i := 0; i < len(result); i++ {
		result[i] = make([]byte, len(box))
	}
	for i := 0; i < len(box[0]); i++ {
		for j := 0; j < len(box); j++ {
			result[i][j] = box[len(box)-1-j][i]
		}
	}
	return result
}
