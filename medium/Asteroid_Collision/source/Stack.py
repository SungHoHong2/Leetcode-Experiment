class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create a stack for collecting the remaining asteroids
        ans = []
        # iterate the asteroids
        for new in asteroids:
            # if there is no asteroid or there is a collision
            while ans and ans[-1] > 0 and new < 0 :
                # get the previous asteroid
                prev = ans[-1]
                # if the new asteroid size is bigger than the previous
                if prev < abs(new):
                    # destroy the previous
                    ans.pop()
                    # continue the loop to add the new asteroid
                    continue
                # if the asteriods collided and the size is the same
                elif prev == abs(new):
                    # destroy the previous
                    ans.pop()
                # end the while loop and do not append the new asterioid
                break
            # add new asteroid if there is no collision
            else:
                ans.append(new)
        # return the stack
        return ans