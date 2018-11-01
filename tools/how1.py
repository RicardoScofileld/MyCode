import re
import sys

def howmuch(n):
    '''给定一个正整数n，实现一个函数，对于区间(0，n]内的每一个整数0<x<=n,计算x对应的二进制数中的1的个数，并计算出函数执行的时间复杂度和空间复杂度'''
    # 参数校验
    if not isinstance(n, int):
        return '请输入一个数字'
    if n <= 0:
        return '请输入一个大于0的数字'
    # 生成列表
    my_list = [i for i in range(1, n+1)]
    # 返回个数
    ones = []
    for i in my_list:
        i = bin(i).lstrip('0b')
        num = len(re.findall(r'1', i))
        ones.append(num)
    # 返回一个列表
    print(ones)

if __name__ == '__main__':
   n = sys.argv[1]
   howmuch(int(n))
