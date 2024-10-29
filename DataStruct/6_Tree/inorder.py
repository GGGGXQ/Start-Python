from pythonds.basic import BinaryTree
import operator


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())


# 修改中序遍历函数，还原完全括号表达式
def print_exp(tree):
    s_value = " "
    if tree:
        s_value = '(' + print_exp(tree.get_left_child())
        s_value = s_value + str(tree.get_root_value())
        s_value = s_value + print_exp(tree.get_right_child()) + ')'
        return s_value