#tạo mảng 3x2, dữ liệu nhập từ bàn phím
#in kq
#cho phép người dùng nhập giá trị tìm kiếm, in ra vị trí, nếu k tìm thấy yêu cầu nhập lại

import numpy as np 

print("Nhập lần lượt các giá trị:")
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

print("Hiển thị danh sách: ")
l = np.array([[a,b],[c,d],[e,f]])

print(l)

g =  l[:,0]
j = list(g)

h = l[:,1]
k = list(h)

n =0
m =0
while n ==0 and m==0:

    x = input("Nhập giá trị cần tìm: ")
    hang = 0
    cot = 0

    for count,i in enumerate(j):
        if i == x:
            hang = count+1
            print("Hàng {}, cột 1".format(hang))
            n =1
    for count,i in enumerate(k):
        if i == x:
            hang = count+1
            print("Hàng {}, cột 2".format(hang))
            m =1
    if n ==0 and m==0:
        print("Không tìm thấy!\n")