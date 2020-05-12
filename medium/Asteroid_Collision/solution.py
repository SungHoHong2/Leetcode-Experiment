class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            # print(new)

            # if the asterioids collide and size is different
            # the new asteroid is moving to the left and the previous asteroid is moving to the right
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue

                # if the asteriods collided and the size is the same
                elif ans[-1] == -new:
                    ans.pop()
                break

            else:
                ans.append(new)

        return ans