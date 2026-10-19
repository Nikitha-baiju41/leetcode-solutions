
class Solution(object):
    def pathSum(self, root, targetSum):
        prefix_sums = {0: 1}

        def dfs(node, current_sum):
            if node is None:
                return 0

            current_sum += node.val
            count = prefix_sums.get(current_sum - targetSum, 0)

            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sums[current_sum] -= 1

            return count

        return dfs(root, 0)
