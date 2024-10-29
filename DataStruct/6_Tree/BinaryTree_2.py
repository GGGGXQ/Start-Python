# 节点与引用
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, new_root):
        self.key = new_root

    def get_root_value(self):
        return self.key

    def preorder2(self):
        print(self.key)
        if self.left_child:
            self.preorder2()
        if self.right_child:
            self.preorder2()


if __name__ == '__main__':
    tree = BinaryTree('a')
    print(tree.get_root_value())
    print(tree.get_left_child())
    print(tree.get_right_child())
    tree.insert_left('b')
    print(tree.get_left_child())
    print(tree.get_left_child().get_root_value())
    print(tree.get_root_value())
    tree.set_root_value('c')
    print(tree.get_root_value())
