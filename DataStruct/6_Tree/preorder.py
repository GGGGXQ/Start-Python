from pythonds.basic import BinaryTree


# 将前序遍历算法实现为外部函数
def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# 将前序遍历算法实现为BinaryTree类的方法
# def preorder2(self):
#     print(self.key)
#     if self.left_child:
#         self.preorder2()
#     if self.right_child:
#         self.preorder2()
# 很少会只做便利操作，还要通过遍历实现别的目标，因此采用外部函数的方式
