from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def printBST(self, root):
        if not root:
            return
        print(root.val)
        self.printBST(root.left)
        self.printBST(root.right)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(root, val):

            if not root:
                return TreeNode(val)  # if reached the end create the new node
            if root.val < val:
                # link new node with parent node (assign to the right pointer)
                root.right = insert(root.right, val)
            elif root.val > val:
                root.left = insert(root.left, val)
            return root

        return insert(root, val)

    def searchInBST(self, root, val):

        if not root:
            return False

        if root.val < val:
            return self.searchInBST(root.right, val)
        elif root.val > val:
            return self.searchInBST(root.left, val)
        else:
            return True

    # looking only in the left subtree, the left most element is the min
    def minValueBST(self, root):
        # recursion not used as we are simply traveling a linked list and not a tree
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def remove(self, root, val):

        if not root:
            return None

        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            # case1: when node to be removed has 0 or 1 child
            # when it has only left child
            if not root.right:
                return root.left
            # when it has only right child
            elif not root.left:
                return root.right
            # Case 2: when node to be removed has 2 children ,find min node in the right subtree and overwrite the node to be removed
            else:
                minNode = self.minValueBST(root.right)
                root.val = minNode.val
                return self.remove(root.right, minNode.val)
        return root

    def bfsTraversal(self, root):

        q = deque()
        if root:
            q.append(root)
        bfs = []
        lvl = 0
        while q:
            print("level", lvl)
            q_len = len(q)
            level = []
            for v in q:
                level.append(v.val)
            # level.append(q[-1].val)  # right view of tree
            bfs.append(level)
            for i in range(q_len):
                curr = q.popleft()
                print(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            lvl += 1
        return bfs


sol = Solution()
root = TreeNode(4)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 5)
sol.insertIntoBST(root, 7)
sol.insertIntoBST(root, 3)
# sol.printBST(root)
# print(sol.minValueBST(root))

# sol.remove(root, 4)
# print("After removing:")
print(sol.bfsTraversal(root))
