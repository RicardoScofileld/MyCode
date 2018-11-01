import copy

def nums(arr, d):
    '''给定一个数组arr和常数d，实现一个函数，计算出在数组arr中，所有距离为d的元素组的数量，并计算出函数执行的时间复杂度和空间复杂度'''
    # 设置变量记录总数
    count = 0
    for i in arr:
        arr1 = copy.copy(arr)
        arr1.remove(i)
        for j in arr1:
            if j-i == d:
                count += 1
    return count 

if __name__ == '__main__':
    arr = [3, 5, 8, 7, 8, 10]
    d = 2
    print(nums(arr,d))
