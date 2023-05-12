#tính tiền cước taxi


while True:
	try:
		x = float(input("\nNhập quãng đường đi đươc: ")) #input
		if x < 0:
			print("Nhập số không âm! ")
		else:
			break

	except:
		print("Định dạng đầu vào không hợp lệ!")


if x <=2:
	a= 10000*x
elif x <=10:
	a= 20000+(x-2)*7000
elif x <= 20:
	a= 20000+ 56000+(x-10)*5000
else:
	a = 20000+56000+50000+(x-20)*3000

print("Tiền cước: ",a, "đ") #output
