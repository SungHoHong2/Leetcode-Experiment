### Minimum Cost Tree From Leaf Values
- Each node has either 0 or 2 children.
- The values of `arr` correspond to the values of each leaf in an in-order traversal of the tre
- The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

---
**Solution 1**
- We remove the element from the smallest to bigger.
- We check the `min(left, right)`
- For each element `a`, `cost = min(left, right) * a`

---
**Solution 2**
- Just find the next greater element in the array, on the left and one right


