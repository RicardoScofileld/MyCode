import sys


def combinations(iterable, r):
    '''从长度为n的列表中，获取长度为m的集合.python内置函数combinations,用来排列组合，抽样不放回'''
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return '长度越界'
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
            else:
                return 
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)


if  __name__ == '__main__':
    iterable = sys.argv[1]
    r = int(sys.argv[2])
    res = combinations(iterable, r)
    for i in res:
        print(i)
