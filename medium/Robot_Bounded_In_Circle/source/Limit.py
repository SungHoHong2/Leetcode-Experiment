class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # set a index for the directions
        idx = 0
        # initial position is in the center
        x = y = 0
        # iterate the instructions
        for i in instructions:
            # go west if moving to the left
            if i == "L":
                idx = (idx + 3) % 4
            # go east if moving to the right
            elif i == "R":
                idx = (idx + 1) % 4
            # increase x,y if moving straight
            elif i == 'G':
                x += directions[idx][0]
                y += directions[idx][1]
        # return true if the robot returns into initial position or the robot doesn't face north
        return (x == 0 and y == 0) or idx != 0