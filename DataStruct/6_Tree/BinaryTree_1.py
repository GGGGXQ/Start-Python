# 列表之列表
# 创建一个二叉树实例
def binary_tree(r):
    return [r, [],[]]


# 返回当前节点的左子节点所对应的二叉树
def get_left_child(root):
    return root[1]


# 返回当前节点的右子节点所对应的二叉树
def get_right_child(root):
    return root[2]


# 在当前节点中存储参数val中的对象
def set_root_value(root, new_root):
    root[0] = new_root


# 返回当前节点存储的对象
def get_root_value(root):
    return root[0]


# 新建一棵二叉树，并将其作为当前节点的左子节点
def insert_left_value(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


# 新建一棵二叉树，并将其作为当前节点的右子节点
def insert_right_value(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])
    return root


if __name__ == '__main__':
    r = binary_tree(3)
    insert_left_value(r, 4)
    insert_right_value(r, 5)
    insert_right_value(r, 6)
    insert_right_value(r, 7)
    print(r)
    l = get_left_child(r)
    print(l)
    set_root_value(r, 9)
    print(r)
