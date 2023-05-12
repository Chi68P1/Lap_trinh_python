#nhập một chuỗi tối đa 10 kí tự và in chuỗi
#in ra màn hình: chiều dài chuỗi, số khoảng trắng
#chuyển chuỗi sang chữ in HOA và in chuỗi

a=11
while a>10:
	x = input("Nhập chuỗi tối đa 10 kí tự:")  #input
	a= len(x)


b=0  #biến đếm khoảng trắng

for i in range(0,a):
	if x[i]==" ":
		b+=1
#ouput		
print("Chuỗi sau khi in HOA: ",x.upper())
print("Số khoảng trắng: ", b)
print("Chiều dài chuỗi: ", a)