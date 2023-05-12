#nhập họ và tên
#chuẩn hóa (chữ đầu viết hoa, toàn bộ viết hoa) và in kq

#input
x = input("Nhập họ và tên: \n") 

#Đưa về chữ thường
x = x.lower()

#tách
A = x.split()

#Viết hoa chữ cái đầu
print("\nHọ và tên sau khi chuẩn hóa: ")
print("Viết hoa chữ cái đâu: ")
for i in A:
	i = i.capitalize()

	print(i ,end= " ") #output


print("\n\nViết hoa toàn bộ:\n"+x.upper()) #output