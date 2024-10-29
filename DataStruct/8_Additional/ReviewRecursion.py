# 简单的取余加密函数(凯撒加密)
import random


def encrypt(m):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 13) % 26
        n = n + s[i]
    return n


# 使用密钥解密
def decrypt(m, k):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = ''
    for i in m:
        j = (s.find(i) + 26-k) % 26
        n = n + s[i]
    return n


# 幂剩余
def modexp(x, n, p):
    if n is 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n//2, p)
    if n%2 is not 0:
        tmp = (tmp * x) % p
    return tmp


# 最大公因数与逆元
# 欧几里得求最大公因数
def gcd(a, b):
    if b is 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(a-b, b)


# 改良后欧几里得算法
def gcd2(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a % b)


# 拓展gcd函数
def ext_gcd(x, y):
    if y is 0:
        return x, 1, 0
    else:
        (d, a, b) = ext_gcd(y, x % y)
        return d, b, a-(x//y)*b


# RSA算法
def RSA_gen_keys(p, q):
    n = p * q
    pq_minus = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(pq_minus, e) is not 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pq_minus, e)
    if b < 0:
        d = pq_minus + b
    else:
        d = b
    return e, d, n


def RSAencrypt(m, e, n):
    chunks = toChunks(m, n.bit_length() // 8 * 2)
    enc_list = []
    for mess_chunk in chunks:
        c = modexp(mess_chunk, e, n)
        enc_list.append(c)
    return enc_list


def RSAdecrypt(chunk_list, d, n):
    r_list = []
    for c in chunk_list:
        m = modexp(c, d, n)
        r_list.append(m)
    return chunksToPlain(r_list, n.bit_length() // 8 * 2)


# 将字符串转换为数字块列表
def toChunks(m, chunkSize):
    byteMess = bytes(m, 'utf-8')
    hexString = ''
    for b in byteMess:
        hexString = hexString + ("%02x" % b)

    numChunks = len(hexString) // chunkSize
    chunk_list = []
    for i in range(0, numChunks*chunkSize-1):
        chunk_list.append(hexString[i:i+chunkSize])
    chunk_list = [eval('0x'+x) for x in chunk_list if x]
    return chunk_list


def chunksToPlain(clist, chunkSize):
    hexList = []
    for c in clist:
        hexString = hex(c)[2:]
        clen = len(hexString)
        hexList.append('0' * ((chunkSize - clen) % 2) + hexString)
        hstring = "".join(hexList)
        messArray = bytearray.fromhex(hstring)
        return messArray.decode('utf-8')
