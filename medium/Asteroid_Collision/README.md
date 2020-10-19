### Asteroid Collision
**Stack**
- [Source code](source/Stack.py)
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create a stack for collecting the remaining asteroids
        # iterate the asteroids 
            # if there is no asteroid or there is a collision
                # get the previous asteroid
                # if the new asteroid size is bigger than the previous 
                    # destroy the previous 
                    # continue the loop to add the new asteroid
                # if the asteriods collided and the size is the same
                    # destroy the previous
                # end the while loop and do not append the new asterioid
            # add new asteroid if there is no collision
        # return the stack
        pass
```

