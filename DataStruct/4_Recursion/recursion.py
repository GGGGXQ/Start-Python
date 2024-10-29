# from turtle import *
#
#
# # 递归求和函数
# def list_sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
#
#
# # 将整数转换成以2~16为基数的字符串
# def to_string(n, base):
#     convert_string = "0123456789ABCDEF"
#     if n < base:
#         return convert_string[n]
#     else:
#         return to_string(n // base, base) + convert_string[n % base]


# 栈帧：实现递归
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return self.items is []
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
#
# rStack = Stack()
#
#
# def to_string(n, base):
#     convert_string = "0123456789ABCDEF"
#     if n < base:
#         rStack.push(convert_string[n])
#     else:
#         rStack.push(convert_string[n % base])
#         to_string(n // base, base)


# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)

# 汉诺塔
def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, to_pole, from_pole, with_pole)

def move_disk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))


if __name__ == '__main__':
    # print(list_sum([1, 3, 5, 7, 9]))
    # my_turtle = Turtle()
    # my_win = my_turtle.getscreen()
    # draw_spiral(my_turtle, 100)
    # my_win.exitonclick()
    move_tower(5, 1, 3, 2)
