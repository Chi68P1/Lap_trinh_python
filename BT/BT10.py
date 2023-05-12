#tạo list có 5 giá trị, các giá tri nhập lần lượt từ bàn phím
#in list
#in max, min, trung bình của list



print("Nhập lần lượt 5 số nguyên: ")
#input
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

#tạo list
f = [a,b,c,d,e] 

#xử lí
g = max(f)
h = min(f)
i = float(sum(f)/5)

#output
print("Các giá trị của list: ",f)
print("Giá trị lớn nhất: ",g)
print("Giá trị nhỏ nhất: ",h)
print("Giá trị trung bình: ",round(i,2))