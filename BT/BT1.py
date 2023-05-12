#nhâp số có 3 chữa số
#in ra màn hình chữ số hàng trăm, chục, đơn vị

#input

x =int(input("Nhập số nguyên có 3 chữ số: \n"))

a = x %10 #đơn vị
b = x-a
c =(b %100)
d =int(c/10)#chục
e= x-c
f= int(e/100)#trăm

#output

print("Số hàng đơn vị:",a)
print("Số hàng chục:",d)
print("Số hàng trăm:",f)