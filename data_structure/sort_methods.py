import random

def bubble_sort(alist):
    '''冒泡排序'''
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

def selection_sort(alist):
    '''选择排序'''
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

def insert_sort(alist):
    '''插入排序'''
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

def quick_sort(alist, start, end):
    '''快速排序'''
    # 递归退出的条件
    if start >= end:
        return
    # 选择一个数为基准
    mid = alist[start]
    # low为从左向右移动的游标
    low = start
    # high为从右到左移动的游标
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

def shell_sort(alist):
    '''希尔排序'''
    n = len(alist)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap // 2

def merge_sort(alist):
    '''归并排序'''
    if len(alist) <= 1:
        return alist
    # 二分法分解
    num = len(alist)//2
    left = merge_sort(len(alist)[:num])
    right = merge_sort(len(alist)[num:])
    return merge(left, right)

def merge(left, right):
    '''合并操作，将两个有序列表进行合并成一个大的有序数组'''
    # left和right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

if __name__ == '__main__':
    alist = [random.randint(0, 100) for i in range(10)]
    print(alist)
    # 冒泡排序
    # bubble_sort(alist)
    # print(alist)

    # 选择排序
    # selection_sort(alist)
    # print(alist)

    # 插入排序
    # insert_sort(alist)
    # print(alist)

    # 快速排序
    # quick_sort(alist, 0, len(alist)-1)
    # print(alist)

    # 希尔排序
    # shell_sort(alist)
    # print(alist)

    # 归并排序
    merge_sort(alist)
    print(alist)