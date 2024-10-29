# 简单的模式匹配器
def simpleMatcher(pattern, text):
    start = 0
    i = 0
    j = 0
    match = False
    stop = False
    while not match and not stop:
        if text[i] is pattern[j]:
            i += 1
            j += 1
        else:
            start = start + 1
            i = start
            j = 0
        if j is len(pattern):
            match = True
        else:
            if i is len(text):
                stop = True
    if match:
        return i-j
    else:
        return -1

