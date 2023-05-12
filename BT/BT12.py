#tạo mảng 5x3
#in ra màn hình
#Người dùng nhập msssv hoặc họ và tên, in ra số điểm tương ứng


import numpy as np 

print("Hiển thị danh sách: ")
a = np.array([["Nguyễn Hữu Chí", 20146479,10],["Lê Đặng Nam", 20146507, 9],["Trần Lê Nhật Huy", 20146494, 8],["Trần Sỹ Việt", 20146544,7],["Nguyễn Minh Trí", 20146540,6]])
print(a)

b = input("\nNhập MSSV hoặc Họ và tên:\n")

c =  a[:,0]
d = list(c)
print(type(c))
print(type(d))
e = a[:,1]
f = list(e)

for i in d:
	if i == b:
		vt = d.index(i)
		print("Điểm tương ứng :",a[vt][2])

for i in f:
	if i == b:
		vt = f.index(i)
		print("Điểm tương ứng :",a[vt][2])


