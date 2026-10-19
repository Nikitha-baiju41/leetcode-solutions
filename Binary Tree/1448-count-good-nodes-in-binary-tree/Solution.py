
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_value):
            if node is None:
                return 0

            count = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, float('-inf'))
