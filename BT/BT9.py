#nhập chuỗi tối đa 50 kí tự
#xóa khoảng trắng và in chuỗi mới

x=51
while x >50:
	a = input("Nhập chuỗi tối đa 50 kí tự: ")  #input
	x = len(a)


b = a.replace(" ","") #thay khoảng trắng bằng rỗng
print(b)   #ouput