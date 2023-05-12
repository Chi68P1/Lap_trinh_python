#nhập vào các giá trị C, L, f
#tính và in ra tổng trở Z

import math  #thư viện

#input
a = float(input("Nhập giá trị điện dung C: "))
b = float(input("Nhập giá trị điện kháng L: "))
c = float(input("Nhập giá trị tần số f: "))

#công thức
d = abs(2*math.pi*c*b-1/(2*math.pi*c*a))
e = round(d,2)

#output
print("Tổng trở Z của mạch: ",e,"ohm")