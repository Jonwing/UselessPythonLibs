# coding:utf-8


class Node:
    """
    二叉树左右枝
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        查找节点
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        return self, parent

    def delete(self, data):
        """
        删除节点
        """
        node, parent = self.lookup(data)

        if node is not None:
            children_count = self.children_count()
            if children_count == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n

                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def children_count(self):
        """
        计算子节点
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def conpare_trees(self, node):
        """
        比较两棵树
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):
        """
        按顺序打印树的内容
        """
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':
    import random
    tree = Node(12)
    for i in range(12):
        tree.insert(random.randint(0, 30))
    print tree.children_count()
    tree.print_tree()
