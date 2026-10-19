
class Solution(object):
    def longestZigZag(self, root):
        self.answer = 0

        def dfs(node):
            if node is None:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            left_length = left[1] + 1
            right_length = right[0] + 1

            self.answer = max(
                self.answer,
                left_length,
                right_length
            )

            return (left_length, right_length)

        dfs(root)
        return self.answer
