import operator
from pythonds.basic import BinaryTree


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child)
        postorder(tree.get_right_child)
        print(tree.get_root_value())
# 常见用途：计算解析树


# 后序求值函数
def postorder_eval(tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return operators[tree.get_root_value()](res1, res2)
        else:
            return tree.get_root_value()
