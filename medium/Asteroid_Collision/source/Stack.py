class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create a stack for collecting the remaining asteroids
        stack = list()
        # iterate the asteroids
        for asteroid in asteroids:
            # case 1: when the left and right asteroids collide with different size
            while stack and stack[-1] > 0 and asteroid < 0:
                left, right = stack[-1], abs(asteroid)
                if left < right:
                    stack.pop()
                else:
                    break
            # case 2: when the left and right asteroids collide with the same size
            if stack and stack[-1] > 0 and asteroid < 0:
                # get the colliding asteroids
                left, right = stack[-1], abs(asteroid)
                # if the asteriods collided and the size is the same
                if left == right:
                    # destroy the both left and right
                    stack.pop()
            # case 3: add new asteroid if there is no collision or right destroys the left
            else:
                stack.append(asteroid)
        # return the stack
        return stack