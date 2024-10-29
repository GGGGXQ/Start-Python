class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

# 向上调整二叉堆
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2

# 往列表尾部插入元素
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

# 向下调整二叉堆
    def perc_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

# 查找最小子节点
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            return i * 2 + 1

# 删除最小元素
    def del_min(self):
        ret_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_value

# 检查二叉堆是否为空
    def is_empty(self):
        return self.current_size is 0

# 返回二叉堆大小
    def size(self):
        return self.current_size

# 根据完整列表构建二叉堆
    def build_heap(self, alist):
        i = len(alist) // 2
        self.heap_list = [0] + alist[:]
        self.current_size = len(alist)
        while i > 0:
            self.perc_down(i)
            i -= 1