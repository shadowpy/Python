

"""
Given a binary tree, populate an array to represent the averages of all of its levels.

tree: 
        1
    2       3
  4   5   6   7

level averages: [1, 2.5, 5.5]
"""



from collections import deque


# Time: O(N)  Space: O(N)
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    levelSum = 0.0
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node's value to the running sum
      levelSum += currentNode.val
      # insert the children of current node to the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    # append the current level's average to the result array
    result.append(levelSum / levelSize)

  return result



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
