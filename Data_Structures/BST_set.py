"""
    A Set data structure implemented via an unbalanced Binary Search Tree (BST).
    
    Features:
    - Average case $O(\log n)$ search, insertion, and Hibbard deletion.
    - Advanced range queries including floor, ceil, and boundary counting.
    - Custom tree analytics tracking total node count and average tree depth.
    
    Note: Because this tree does not self-balance (like an AVL or Red-Black tree), 
    worst-case operations degrade to $O(n)$ if elements are inserted in a sorted order.
    """


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None    
    
class TreeSet:
    def __init__(self):
        self.root = None
        self.sizeValue = 0

    def innerContains(self, node, x):
        if not node:
            return False
        if x < node.val:
            return self.innerContains(node.left, x)
        elif x > node.val:
            return self.innerContains(node.right, x)
        else:
            return True

    def contains(self, x):
        return self.innerContains(self.root, x)

    def innerAdd(self, node, x):
        if not node:
            self.sizeValue += 1
            return Node(x)  
        if x < node.val:
            node.left = self.innerAdd(node.left, x)
        elif x > node.val:
            node.right = self.innerAdd(node.right, x)
        return node

    def add(self, x):
        self.root = self.innerAdd(self.root, x)

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def innerRemove(self, node, x):
        if not node:
            return node
        if x < node.val:
            node.left = self.innerRemove(node.left, x)
        elif x > node.val:
            node.right = self.innerRemove(node.right, x)
        else:
            if not node.left:
                self.sizeValue -= 1
                return node.right
            elif not node.right:
                self.sizeValue -= 1
                return node.left

            temp = self.minValueNode(node.right)
            node.val = temp.val
            node.right = self.innerRemove(node.right, temp.val)

        return node

    def remove(self, x):
        self.root = self.innerRemove(self.root, x)

    def innerMin(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node.val

    def min(self):
        return self.innerMin(self.root)

    def innerMax(self, node):
        if not node:
            return None
        while node.right:
            node = node.right
        return node.val

    def max(self):
        return self.innerMax(self.root)

    def size(self):
        return self.sizeValue  

    def innerCount(self, node, lo, hi):
        if not node:
            return 0
        if node.val < lo:
            return self.innerCount(node.right, lo, hi)
        elif node.val > hi:
            return self.innerCount(node.left, lo, hi)
        else:
            return 1 + self.innerCount(node.left, lo, hi) + self.innerCount(node.right, lo, hi)

    def count(self, lo, hi):
        return self.innerCount(self.root, lo, hi)
    
    def ceil(self, x):
        current_ = self.root
        ceil_val = None
        while current_:
            if current_.val >= x:
                ceil_val = current_.val
                current_ = current_.left
            else:
                current_ = current_.right
        return ceil_val

    def floor(self, x):
        current_ = self.root
        floor_val = None
        while current_:
            if current_.val <= x:
                floor_val = current_.val
                current_ = current_.right
            else:
                current_ = current_.left
        return floor_val

    def avg_tree_depth(self):
        if not self.root:
            return None
        total_depth, total_node = self._sum_depths(self.root, 0)
        return total_depth / total_node

    def _sum_depths(self, node, depth):
        if not node:
            return (0, 0)
        left_depth, left_node = self._sum_depths(node.left, depth + 1)
        right_depth, right_nodes = self._sum_depths(node.right, depth + 1)
        return (left_depth + right_depth + depth,left_node + right_nodes + 1)

