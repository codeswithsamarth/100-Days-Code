# from asyncio.streams import FlowControlMixin
#
#
# def Greet():
#     print("Hello World!")
#
# Greet()
#
# lis1 = [True,True,True,False,
#         True,True,True,True,
#         True,False,True,False,
#         True,False,False,True,
#         True,True,True,True,
#         False,False,True,True]
#
# print(lis1.count(True))
# # num = int(input("Enter The Number"))
# # if num < 0:
# #     print(abs(num))
# # else:
# #     print(-num)
# #
# sum = 0
# nums = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# count = 0
# for num in nums:
#     if num > 0:
#         count += 1
#     if (num<0):
#         sum += num
#     if nums == []:
#         print('[]')
#
# print(count,sum)
#
# # word = input("Enter The Word")
# # reverse = word[::-1]
# # print(reverse)
#
#
# list_bool = [True,False,True,False]
# yes = list(map(lambda x: 'Yes' if x else 'No',list_bool))
# print(yes)

l1 = [6,2,1,8,10]
l2 = [1,1,11,2,3]

greatest_two = sorted(l1) [-2:]
greatest_sum = sum(greatest_two)
lowest_two = sorted(l2)[:2]
lowest_sum = sum(lowest_two)

print(lowest_sum,greatest_sum)