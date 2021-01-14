class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create a stack for collecting the remaining asteroids
        stack = list()
        # iterate the asteroids
        for asteroid in asteroids:
            # set the flag for checking collision
            collided = False
            # when the left and right asteroids collides
            while stack and stack[-1] > 0 and asteroid < 0:
                left, right = stack[-1], abs(asteroid)
                # if the left asteroid is destroyed
                if left < right:
                    stack.pop()
                # if the right asteroid is destroyed
                elif left > right:
                    collided = True
                    break
                # if both asteroids are destroyed
                else:
                    stack.pop()
                    collided = True
                    break
            # add a new asteroid in the stack if there is no collision
            if not collided:
                stack.append(asteroid)
        # return the stack
        return stack