from pythonds.basic import Stack
from pythonds.basic import BinaryTree


def build_parse_tree(tree):
    fp_list = tree.split()
    p_stack = Stack()
    e_tree = BinaryTree(' ')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i is '(':
            current_tree.insert_left(' ')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/':
            current_tree.set_left_child(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_value(i)
            current_tree.insert_right(' ')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i is ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return e_tree
