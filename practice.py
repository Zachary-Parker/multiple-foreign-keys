import pickle
# from time import time
#
#
# def sub(x,y):
#     return x - y
#
# def timer(f):
#     def inner(x,y):
#         before = time()
#         rv = f(x,y)
#         print('Elapsed {}'.format(time()-before))
#         return rv
#     return inner
# def func(one_string):
#     if '.' not in one_string:
#         return False
#     elif one_string.count('.') != 3:
#         return False
#     else:
#         flag = True
#         one_list = one_string.split('.')
#         for i in one_list:
#             try:
#                 one_num = int(i)
#                 if one_num >= 0 and one_num <= 255:
#                     pass
#                 else:
#                     flag = False
#             except:
#                 flag = False
#         return flag
# print(func('12.232.2.2'))
#
# def partition(li,left,right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp:
#             right -= 1
#         li[left] = li[right]
#         while left < right and li[left] <= tmp:
#             left += 1
#         li[right] = li[left]
#     li[left] = tmp
#     return left
#
# def quick_sort(li,left,right):
#     if left < right:
#         mid = partition(li,left,right)
#         quick_sort(li,left,mid-1)
#         quick_sort(li,mid+1,right)
#     return li
# import random
#
# li = list(range(1,10001))
# random.shuffle(li)
# print(li)
# print(quick_sort(li,0,len(li)-1))
myDic = {'a':1,'b':2}




