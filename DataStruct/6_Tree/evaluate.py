# 计算二叉解析树的递归函数
import operator


def evaluate(parse_tree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()
    if left_c and right_c:
        fn = operators[parse_tree.get_root_value()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_value()