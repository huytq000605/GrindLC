# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set([(0, 0, 0)])
        ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def move_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(r, c, d):
            for dd in range(4):
                nd = (d + dd) % 4
                nr, nc = r + ds[nd][0], c + ds[nd][1]
                if (nr, nc, nd) not in visited and robot.move():
                    robot.clean()
                    visited.add((nr, nc, nd))
                    dfs(nr, nc, nd)
                    move_back()
                robot.turnRight()
        robot.clean()
        dfs(0, 0, 0)
        
