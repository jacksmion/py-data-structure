# -*- coding:utf-8 -*-

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal(object):
    def __init__(self):
        self.traverse_path = deque()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)

    def levelorder(self, root):
        queue = deque()
        queue.append(root)
        try:
            while True:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                self.traverse_path.append(node.val)
        except IndexError:
            return

    def show_path(self):
        print self.traverse_path


def main():
    node_a = TreeNode("A")
    node_b = TreeNode("B")
    node_c = TreeNode("C")
    node_d = TreeNode("D")
    node_e = TreeNode("E")
    node_f = TreeNode("F")
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    traveror = Traversal()
    traveror.levelorder(node_a)
    traveror.show_path()

main()