# 字符串简单散列函数
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * pos
    return sum % tablesize

