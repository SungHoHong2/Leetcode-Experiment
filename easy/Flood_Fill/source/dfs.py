class Solution:

    def depthFirst(self, sr, sc):

        # out of limit
        if not (0 <= sr < len(self.color)) or not (0 <= sc < len(self.color[0])):
            return False

            # if it is not the pond
        if self.color[sr][sc] != self.oldColor:
            return False

            # print(sr, sc, self.color[sr][sc])
        if self.color[sr][sc] == self.oldColor:
            self.color[sr][sc] = self.newColor
            self.depthFirst(sr - 1, sc)
            self.depthFirst(sr + 1, sc)
            self.depthFirst(sr, sc - 1)
            self.depthFirst(sr, sc + 1)

        return True

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        # if the new color and the color of the cluster is the same
        if image[sr][sc] == newColor:
            return image

        self.color = image
        self.oldColor = image[sr][sc]
        self.newColor = newColor
        self.depthFirst(sr, sc)
        return self.color