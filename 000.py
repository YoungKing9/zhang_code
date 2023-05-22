# li1 = [1,3,5]
# li2 = [7,8,9]
# for i in li1:
#     if i < 6:
#         print('one_if', i)
#         if i > 0:
#             break
dic = {}
li = ['shoes', 'bin', 'pedestal', 'wire', 'socket', 'cat', 'dog', 'desk_rect', 'desk_circle', 'weighing-scale']
num = 0
for i in li:
    dic[num] = i
    num += 1

print(dic)
